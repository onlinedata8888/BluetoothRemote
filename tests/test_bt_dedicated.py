import os
from playwright.sync_api import sync_playwright
HTML = 'file://' + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app', 'assets', 'remote.html'))
src = open(os.path.join(os.path.dirname(__file__), 'test_bt_pad.py')).read()
FAKE = open(os.path.join(os.path.dirname(__file__), 'test_trackpad_page.py')).read().split('FAKE = """')[1].split('"""')[0]
HIDF = src.split('HIDF = """')[1].split('"""')[0]
res = []
def check(n, c, extra=''):
    res.append(bool(c)); print(('PASS' if c else 'FAIL'), '-', n, extra)
with sync_playwright() as p:
    b = p.chromium.launch(); ctx = b.new_context(viewport={'width': 390, 'height': 844}, has_touch=True); pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e))); pg.add_init_script(FAKE); pg.add_init_script(HIDF); pg.goto(HTML); pg.wait_for_timeout(500)
    pg.locator('#gtOpenBtn').click(); pg.wait_for_timeout(450)
    pg.locator('#gtBtOpen').click(); pg.wait_for_timeout(500)
    ks = pg.evaluate("[...document.querySelectorAll('#btpKeys .btp-key')].map(k=>k.dataset.k)")
    for k in ['back','home','mute','volDown','volUp','mic','kb']: check('default has ' + k, k in ks)
    check('12 default keys', len(ks) == 12, ks)
    pg.evaluate('window.__h = []')
    exp = {'back':0x224,'home':0x223,'mute':0xE2,'volUp':0xE9,'volDown':0xEA,'mic':0xCF}
    for k, u in exp.items():
        bb = pg.locator('#btpKeys [data-k="%s"]' % k).first.bounding_box()
        pg.mouse.click(bb['x'] + bb['width']/2, bb['y'] + bb['height']/2); pg.wait_for_timeout(80)
    h = pg.evaluate('window.__h'); got = [x[1] for x in h if x[0] == 'consumer']
    check('consumer keys sent over Bluetooth', got == list(exp.values()), got)
    pg.locator('#btpKeys [data-k="kb"]').first.click(); pg.wait_for_timeout(200)
    check('keyboard opens', 'open' in pg.locator('#btpKb').get_attribute('class'))
    pg.locator('#btpKbDone').click()
    # trackpad: swipe right = arrow key, tap = Enter, never mouse move
    pg.evaluate('window.__h = []')
    r = pg.locator('#btpPad').bounding_box(); cx, cy = r['x'] + r['width']/2, r['y'] + r['height']/2
    cdp = ctx.new_cdp_session(pg)
    def touch(t, x, y): cdp.send('Input.dispatchTouchEvent', {'type': t, 'touchPoints': ([{'x': x, 'y': y}] if t != 'touchEnd' else [])})
    touch('touchStart', cx, cy); 
    for i in range(1, 8): touch('touchMove', cx + i*12, cy)
    touch('touchEnd', 0, 0); pg.wait_for_timeout(100)
    h = pg.evaluate('window.__h'); check('swipe right -> HID key 0x4F', ['key', 0x4F, 0] in h, h)
    pg.evaluate('window.__h = []')
    touch('touchStart', cx, cy); touch('touchEnd', 0, 0); pg.wait_for_timeout(100)
    h = pg.evaluate('window.__h'); check('tap -> HID key Enter 0x28', ['key', 0x28, 0] in h, h)
    check('no mouse move / click', not any(x[0] in ('move', 'click', 'buttons') for x in h + pg.evaluate('window.__h')))
    check('no page errors', not errs, errs)
    b.close()
print('%d/%d' % (sum(res), len(res)))
