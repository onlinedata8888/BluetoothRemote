# Remote2 42 - TV keyboard: Play Store जैसे दूसरे apps में भी type हो (YouTube वैसा ही रहता है)

## क्यों Play Store में type नहीं हो रहा था (सबसे संभावित वजह)
TV हर text edit के साथ उस text box का "field counter" माँगता है। नया box खुलने पर (Play Store search) TV नया counter भेजता है,
पर v41 पुराना counter इस्तेमाल करता था (जो YouTube वाले आख़िरी batch edit से मिला था)। गलत counter वाला edit TV चुपचाप छोड़ देता है।

## v42 में
- **सबसे ताज़ा counter:** TV की जो भी report सबसे आख़िर में आई (नया text box ya पिछले edit का echo), उसी का counter लगता है।
- **Safe retry:** जिस TV के बारे में पता है कि वो हर बदलाव की report वापस भेजता है (यह app खुद सीखकर save कर लेता है),
  वहाँ अगर 1.2 सेकंड में report नहीं आई तो मतलब edit छोड़ दिया गया। तब वही text अगले counter तरीके से **एक बार** दोबारा भेजा जाता है
  (4 तरीके तक)। जो तरीका चला वो याद रहता है।
- **Fallback:** चारों तरीके छोड़े गए तो वही text normal key presses से **एक बार** टाइप होता है, और keyboard hint में बताया जाता है
  कि TV पर search box चुनकर OK दबाओ ताकि TV का keyboard खुले।
- **YouTube जैसा था वैसा:** जो TV report वापस नहीं भेजता वहाँ कभी दोबारा नहीं भेजता (यही v39 में 4 बार type होने की वजह थी)।
- Backspace पहले जैसा: हर बार एक DEL, TV पर पहले से लिखा text भी delete होता है।
- Keyboard hint में अब TV का text box label भी दिखता है (जैसे "Search")।

## Files
RemoteSession.java, TvBridge.java, app/assets/remote.html, tests/ImeTest.java (fake TV, 9 scenarios / 36 checks), tests/test_tv_keyboard.py (34 checks).
On-screen version: v2.42
