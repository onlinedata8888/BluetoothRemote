# Remote67 Kb
- Mobile Style Panel, Edit mode: two switches "Home gesture" / "Recent gesture" (both ON by default, saved with the layout, Reset = both ON).
- Recent gesture: swipe UP from the area below the box and keep the finger still (~0.45 s) = Recent. Lifting before that = Home. If "Recent gesture" is OFF, Home fires immediately at the swipe; if "Home gesture" is OFF, only the hold gives Recent; both OFF = no bottom gesture.
- New widget "Menu line" (Edit mode palette, can be added anywhere): a thin line; swipe RIGHT -> LEFT on it = TV menu (same key as the top-left 3-line Menu button). Invisible hit padding around the line, movable, width/height sliders go down to 6 px, saved with the layout.
- Panel tip text follows the switches. Stage has touch-action:none so vertical swipes are not stolen by the WebView.
- Tests: tests/test_gt_gestures.py (21 checks); test_trackpad_page.py cleaned of the removed in-pad Home/Recent checks (38 checks).
