Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
=============== RESTART: C:/Users/Kiruthika/Desktop/daa/daa 2.py ===============
Text    : AABAACAADAABAABA
Pattern : AABA

Naive      -> Matches at: [0, 9, 12], Comparisons: 30
KMP        -> Matches at: [0, 9, 12], Comparisons: 20
Rabin-Karp -> Matches at: [0, 9, 12], Comparisons: 12

     Pattern      Naive        KMP         RK
----------------------------------------------
          AB      12542      11901       1284
        ABCD      13337      12506        229
      ABCDAB      13378      12541        170
    ABCDABCD      13378      12543        128
