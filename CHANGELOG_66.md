# Remote66 Kb
- Mobile Style Panel: the pad no longer has a Back swipe from its own left/right edge. Swiping from inside the box is now a normal touchpad move (arrows) and never triggers Back. The little white edge bars inside the pad (marking the old in-pad Back zone) were removed too.
- Back swipe from the OUTER area around the pad (left/right side of the panel) is unchanged.
- tests/test_trackpad_page.py: in-pad edge swipe now asserts "NO Back".
- Back swipe zone (outer left/right strips) now exists only level with the pad box: same top-to-bottom as the box, follows its size/position. Above or below the box there is no Back swipe.
- Home gesture added back: swipe UP starting in the area below the pad box = Home (inside the box it stays a normal touchpad move; above the box nothing).
