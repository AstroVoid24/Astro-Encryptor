import os
import time
home_folder = os.path.expanduser("~")
file_path = home_folder + "/Desktop/custom-lang.astro"
while True:
    print("""
    Welcome to the: 
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
    🟩🟩🟩\033[1m\033[32m&#$* > John\033[32m\033[1m🟩🟩🟩
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩

    SECRET LANGUAGE MAKER
     \033[0mBy \033[95mAstroVoid24""")
    choice1 = input("""\033[0mWhat do you like to do?
        CUSTOM LANGUAGE > Eng - \"1\"
        Eng > CUSTOM LANGUAGE - \"2\"
        CUSTOM LANGUAGE MAKER - \"3\"
        Automatic language maker(Not Recommended!) - \"4\"
        Answer: """)
    if choice1 == "3":
            FullLanguage = []
            print(f"""Tutorial:
            Type the symbol of your language and then type the english letter
            And hit enter to go to the next letter
            Example: &a *Hits enter
                     %b *Hits enter
            It asks 42 pairs, but alphabet is only 26?
            True, but there are other important symbols and more importantly NUMBERS!
            The extra symbols: 1234567890,.=+-%?
            dont put \\q, It will mess up
            It's recommended to put english letters alphabetically, then numbers, then the other symbols
            To send it to you friend or someone, send the \"custom-lang.astro\" in your desktop to them and
            they should put it in their desktop""")
            for LineLetter in range(43):
                pair = input(f"ExtraSym: 1234567890,.=+-%? | Letter {LineLetter + 1}:")
                FullLanguage.append(pair)
            with open(file_path, "w") as f:
                for pair in FullLanguage:
                    f.write(pair + "\n")
            with open(file_path, "r") as file:
                Review = file.read()
                print("Everything is done!\nJust hit enter to go to the main menu\nReview your translation!:")
                time.sleep(1)
            ReviewInputWait = input(f"{Review}")
            if ReviewInputWait == ReviewInputWait:
                pass
    if choice1 == "4":
        with open(file_path, "w") as f:
                f.write("""!a
@b
#c
$d
%e
^f
&g
*h
(i
)j
_k
-l
=m
+n
~o
`p
{q
}r
[s
]t
|u
:v
;w
<x
>y
?z
A0
B1
C2
D3
E4
F5
G6
H7
I8
J9
K,
L.
M=
N+
O-
P%
Z?""")
        print("Done! (1sec delay)")
        time.sleep(1)
    elif choice1 == "2":
        Translation = {}
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if line:  # skip empty lines
                    symbol = line[:-1]
                    letter = line[-1]
                    Translation[letter] = symbol

        FromEnglish = input("Text: ")
        result = ""
        for char in FromEnglish:
            if char in Translation:
                result += Translation[char]
            else:
                result += char  # (optional) keep unknown characters
        WaitTranslation1 = input(f"{FromEnglish} -> {result}\nJust hit enter to go to the main menu")
        if WaitTranslation1 == WaitTranslation1:
            pass
    elif choice1 == "1":
        TranslationToEng = {}
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if line:  # skip empty lines
                    symbol = line[:-1]
                    letter = line[-1]
                    TranslationToEng[symbol] = letter

        # Phase 2: Translate and print
        ToEnglish = input("Text: ")
        result = ""
        for char in ToEnglish:
            if char in TranslationToEng:
                result += TranslationToEng[char]
            else:
                result += char  # (optional) keep unknown characters
        WaitTranslation2 = input(f"{ToEnglish} -> {result}\nJust hit enter to go to the main menu")
        if WaitTranslation2 == WaitTranslation2:
            pass
    else:
        print(f"Typo: {choice1}\n2 Second pause")
        time.sleep(2)
