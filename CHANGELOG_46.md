# Remote2 46 - TV keyboard khud khule + har app ke liye alag learning

- **Keyboard khud khulta hai:** TV jab text box focus kare (RemoteImeShowRequest) to phone ka keyboard apne aap khul jata hai (Google TV remote jaisa).
  Aap band karo to 2.5 s tak dobara nahi khulta.
- **App-wise learning:** pehle "TV har edit report karta hai" ek TV ke liye save hota tha (YouTube se). Ab TV app (package) ke hisaab se save hota hai,
  isliye YouTube ka behaviour Play Store / dusre apps par laga nahi hota (ye retry/duplicate ki ek wajah thi).
- **Jo app report nahi karta (Play Store, 3rd party):** apne bheje edits gin kar IME counter aage badhta hai, taaki doosra edit purane counter se na jaye
  ("sirf pehli baar chalta hai" wali problem ka ilaaj).
- **Keyboard log:** keyboard ke neeche "Keyboard log" par tap karo -> TV aur phone ke beech ke IME messages dikhte hain (copy bhi ho jata hai).
  Agar koi app abhi bhi na chale to wo log bhejo.

Files: RemoteSession.java, TvBridge.java, app/assets/remote.html, tests/ImeTest.java (35 checks pass).
