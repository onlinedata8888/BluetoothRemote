# Remote5 1 - naya Trackpad page (phone jaisa gestures)

- **Shortcut:** 1st page ke touchpad ke left corner me (navigation icon ke samne) naya **phone icon**. Tap karo -> Trackpad page khulta hai.
- **Trackpad:** ek rectangle pad. Ungli move = up / down / left / right, tap = OK, kisi taraf ungli le jaa kar hold = lagataar (continuous) chalta rehta hai, ungli hatao to ruk jata hai. Pad par 0.5 s hold = OK long-press.
- **Phone jaise gestures (pad ke bahar ka area):** left ya right side se andar ki taraf swipe = **Back**, neeche se upar swipe = **Recent**.
- **Editable (Edit button):** pad ka size slider se ya corner kheench kar chhota / bada, pad ko drag karke kahin bhi rakho. Remote ke koi bhi button (Back, Home, Recent, OK, Menu, Vol, CH, Mute, media, Settings, Power ...) jodo, drag karke jagah badlo, x se hatao. Layout save rehta hai. Reset se default.
- Android Back se ye page band hota hai (pehle edit mode, phir page).

Files: app/assets/remote.html, tests/test_trackpad_page.py (22 checks pass).
- v2.49: Edit mode me button ka red x ab sahi se delete karta hai (pehle pointer capture ki wajah se click nahi lagta tha), x bada bhi kiya.
- v2.50: Edit mode me har button ka size alag se chhota/bada: button par tap karo (select, hara ghera) -> Btn W / Btn H slider ya button ke neeche-daayein corner ka hara handle kheencho.
