# Remote2 38 - Page-1 TV keyboard rewritten (Android TV Remote v2)

Purana keyboard (HTML + CSS + JS aur Java ka text/IME code) poora hata ke naya likha gaya.

## Ab sirf EK keyboard
- Custom on-screen keys aur "Phone kb" toggle hata diye. Keyboard button dabao -> phone ka apna default keyboard khulta hai.
- Neeche do button: "Enter / Search" aur "Done". Pairing ka 6-char code bhi isi se jata hai.

## Purana kyun nahi chalta tha
- Har key par sirf ek akshar bheja jata tha, pura text nahi.
- TV ke counters ghalat/purane rehte the, to TV edit ignore kar deta tha (delete chalta tha, naya akshar nahi).
- Koi check nahi tha ki TV ne text liya ya nahi.

## Naya (v2 protocol)
- TV ke messages 20/21/22 padhe jate hain (field counter, ime counter, field ka text).
- Har baar POORA text ek RemoteImeBatchEdit me jata hai. Tez typing me 70 ms me jama karke sirf latest text bhejta hai.
- Bhejne ke baad TV ka apna report dekha jata hai. TV ne text nahi liya to agle counter recipe se dobara bhejta hai
  (4 recipe), jo recipe chali use yaad rakhta hai. Jis TV ka report hi nahi aata, wahan dobara nahi bhejta (duplicate nahi).
- Delete = KEYCODE_DEL, Enter = KEYCODE_ENTER.
- TV par text box khula hi nahi to fallback: normal key presses (sirf lowercase/digits/common symbols).

## Files
RemoteSession.java, Msgs.java, TvBridge.java, app/assets/remote.html,
tests/test_tv_keyboard.py (18 checks), tests/ImeTest.java (fake TV, 4 counter recipes).

## Note
Asli TV par live test yahan nahi ho sakta. Agar phir bhi type na ho to Play Store search box khol kar ek akshar type karo
aur mujhe batao ki hint line kya dikha rahi hai ("Typing into the TV text box" ya "Open a search...").
