# Remote65 Kb
- Bluetooth Pad page: Edit mode is a free layout. The touchpad and every key can be moved (drag) and resized (green corner handle, or the W / H sliders for the selected item). Layout saved (remote13_btp_layout2); old saved layouts convert automatically. Reset = default.
- Every button / widget of the Mobile Style page can now be added to the Bluetooth Pad (same one can be added many times), all over Bluetooth HID (no Java change):
  - Buttons: Back, Home, Recent (consumer 0x1A0), OK, Menu, Search (0x221), arrows, Vol +/-, Mute, CH +/- (0x9C/0x9D), Play, Prev, Next, Rew (0xB4), FF (0xB3), Settings (0x183), Power (0x30), Mic, Keyboard (+ Esc, L/R click, wheel up/down).
  - Widgets: Scroll bar (vertical / horizontal = mouse wheel), Volume bar (vertical / horizontal = Vol+/Vol-), Nav bar (arrows + OK), extra Touchpad (second Bluetooth mouse pad).
- Recent / Settings / Power depend on the TV accepting those Bluetooth consumer keys (Android TV usually does; some TVs ignore them).
- Tests: tests/test_bt_pad.py (36 checks), tests/test_bt_pad_widgets.py (41 checks).
- Panels: "Mobile Style" -> "Mobile Style Panel", "Bluetooth Pad" -> "Bluetooth Remote Panel". Both panels share the same bottom bar: Back | Mobile Style icon | Bluetooth icon (fixed positions). The icon of the open panel is highlighted; tapping the other icon switches panel. Back = the remote. Test: tests/test_panel_tabs.py (12 checks).
- Mobile Style Panel and Bluetooth Remote Panel now slide in from the right (right -> left) instead of from the bottom.
