# Remote5 12b - page-1 keyboard = Remote2 41 keyboard
- Page-1 TV keyboard ported 1:1 from Remote2 41: typing goes through the TV IME text box (ONE RemoteImeBatchEdit per typed part, insert=1, counters from the TV's last batch edit), no confirm / no retry (nothing typed twice).
- Backspace = DEL key each time (old TV text deletes too), Enter/Done = ENTER key, Hindi etc. works. Key-press fallback only when the TV reports no text box.
- Files: RemoteSession.java, TvBridge.java, Msgs.java, app/assets/remote.html (keyboard hint/handlers), tests/ImeTest.java, tests/test_tv_keyboard.py.
- Removed 5.11's key-press-only typing, "no-echo app" recipe/retry logic, keyboard log, auto-open from TV.
- All other 5.12 features untouched. Tests: ImeTest ALL OK, test_tv_keyboard 31/31.
