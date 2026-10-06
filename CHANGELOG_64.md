# Remote64 Kb
- NEW "Bluetooth Pad" page: opened by the Bluetooth icon next to the back arrow (bottom) on the Mobile Style page.
  - Trackpad in the middle: 1 finger = cursor, tap = left click, hold + move = drag, 2 fingers = scroll, 2 finger tap = right click.
  - Keys under it (default): Back, Home, Mic, Keyboard, Vol-, Vol+. Edit: remove with x, add from the list (Mute, Menu, Play, Prev, Next, Enter, Esc, arrows, clicks, scroll). Layout saved. Back arrow at the bottom-left.
  - Everything goes out over Bluetooth HID (no Wi-Fi needed). Keyboard types English letters / numbers / symbols as real HID keys.
- HidMouse.java: new Consumer-control report (ID 4) + HID.consumer(usage) for Home / Back / Volume / Mic. Re-pair the phone once (Forget on TV and phone) because the HID descriptor changed.
- Tests: tests/test_bt_pad.py (23 checks).
