# Remote2 44 - Mouse mode: Bluetooth on karne ka zabardasti prompt band

## Wajah
Bluetooth band hone par app "Bluetooth on karo" screen kholta tha. Wapas aane par app khud phir wahi screen kholta tha
(onResume -> begin -> dobara), aur app focus par auto-reconnect bhi yahi chalata tha. Isliye loop banta tha aur app chalne nahi deta tha.

## v44
- Permission / Bluetooth-on screen ab sirf EK baar aati hai. Aap "nahi" karo to app yaad rakhta hai (btDeclined) aur dobara kabhi nahi poochta.
- Auto-reconnect (focus / resume / mouse mode) ab kabhi koi dialog nahi kholta. Mouse page par bas status likha rehta hai ("Bluetooth on karo").
- Dobara poochna ho to mouse page ka device button ya Bluetooth status par khud tap karo.
- Page 1 (TV remote, WiFi) par Bluetooth ka koi asar nahi.

## Files
HidMouse.java (start/startUser/begin/reconnect), app/assets/remote.html (taps -> startUser, version v2.44).
