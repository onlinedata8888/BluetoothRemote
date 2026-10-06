# Remote5 11 - TV keyboard fix (page 1 keyboard "no-echo app" error)
- Problem: keyboard sent text as IME edits (ime=0,1,2,3 field=0) even when the TV had NOT reported any focused text box, so the TV ignored every letter ("Keyboard log" showed only "no-echo app" lines).
- Fix: IME edits are used ONLY while the TV has reported a focused text box (text status / show request / batch edit). New app in front, or the TV says "no text box" -> that state is cleared.
- When no text box is reported, letters go as normal key presses (like a physical keyboard) so search boxes in any app still receive them. Backspace / Enter always work as keys.
- Keyboard hint now says what is happening (keys mode) instead of claiming "Typing into the TV text box".
- Files: RemoteSession.java, app/assets/remote.html. tests/ImeTest.java: ALL OK.

## 5.11 (2nd fix)
- Typing no longer uses IME edits at all. Every letter/number/Backspace/Enter goes as a normal key press - the same way the number-pad keys already work.
- Removed: keyboard log button, auto-opening of the keyboard from the TV. Pairing-code entry unchanged.
