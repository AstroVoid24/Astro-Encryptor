import os
import readchar
import time
SReadlineDelay = 0.3
SCustomLangPairs = 43
home_folder = os.path.expanduser("~")
file_path = home_folder + "/Desktop/custom-lang.astro"
Sfile_path = home_folder + "/Documents/Misc.astro"
if os.path.exists(Sfile_path):
    with open(Sfile_path, "r") as f:
        line1 = f.readline().strip()
        line2 = f.readline().strip()
        line3 = f.readline().strip()
        if line1: SReadlineDelay = int(float(line1))
        if line2: SCustomLangPairs = int(line2)
        if line3: file_path = line3
else:
    with open(Sfile_path, "w") as f:
        f.write(str(SReadlineDelay) + "\n")
        f.write(str(SCustomLangPairs) + "\n")
        f.write(str(file_path) + "\n")
while True:
    print("\n" * 100)
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
        Pair list - \"5\"
        Settings(will keep getting bigger) - \"6\"
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
            for LineLetter in range(SCustomLangPairs):
                pair = input(f"ExtraSym: 1234567890,.=+-%? | Letter {LineLetter + 1}:")
                FullLanguage.append(pair)
            with open(file_path, "w") as f:
                for pair in FullLanguage:
                    f.write(pair + "\n")
            with open(file_path, "r") as file:
                Review = file.read()
                print("Everything is done!\nReview your translation!:")
                time.sleep(1)
                print(Review + "\n Press any key to continue")
                key = readchar.readkey()
    elif choice1 == "4":
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
        print("Done! Press any key to continue")
        key = readchar.readkey()
    elif choice1 == "2":
        if not os.path.exists(file_path):
            print("No language file found. Please create one first (options 3 or 4).")
            time.sleep(2)
        else:
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
                elif char == " ":
                    result += " "
                else:
                    print("Won't translate! Couldn't find one of the letters, try to write lowercase letters ok? I won't continue becuz if i continue,\nyou could read the whole thing just without 1 letter or 2 and\nI don't know who is in this compyter!")
                    result = ""
                    break
            print(f"{FromEnglish} -> {result}\nPress any key to continue")
            key = readchar.readkey()
    elif choice1 == "1":
        if not os.path.exists(file_path):
            print("No language file found. Please create one first (options 3 or 4).")
            time.sleep(2)
        else:
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
                elif char == " ":
                    result += " "
                else:
                    print("Won't translate! Couldn't find one of the letters, try to write lowercase letters ok? I won't continue becuz if i continue,\nyou could read the whole thing just without 1 letter or 2 and\nI don't know who is in this compyter!")
                    result = ""
                    break
            print(f"{ToEnglish} -> {result}\nPress any key to continue")
            key = readchar.readkey()
    elif choice1 == "5":
        if not os.path.exists(file_path):
            print("No language file found. Please create one first (options 3 or 4).")
            time.sleep(2)
        else:
            print("Current Pairs:")
            time.sleep(1)
            with open(file_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        print(line)
                        time.sleep(SReadlineDelay)
            print("Press any key to continue")
            key = readchar.readkey()
    elif choice1 == "6":
        SExit = True
        while SExit:
            print("\n" * 100)
            print("""⚙ Settings ⚙
    1 - Exit
    2 - Custom Language pair output delay - int/number
    3 - Custom language pairs - int/number
    4 - custom-lang.astro filepath - str/text""")
            choice2 = input("Enter your choice: ")
            if choice2 == "1":
                SExit = False
            elif choice2 == "2":
                try:
                    SReadlineDelay = int(float(input("\nEnter Integer/number: ")))
                except ValueError:
                    print("String Detected, didn't change the value, Press any key to continue")
                    key = readchar.readkey()
                else:
                    print("Done! Press any key to continue")
                    with open(Sfile_path, "w") as f:
                        f.write(str(SReadlineDelay) + "\n")
                        f.write(str(SCustomLangPairs) + "\n")
                        f.write(str(file_path) + "\n")
                    key = readchar.readkey()
            elif choice2 == "3":
                try:
                    SCustomLangPairs = int(float(input("\nEnter Integer/number: ")))
                except ValueError:
                    print("String Detected, didn't change the value, Press any key to continue")
                    key = readchar.readkey()
                else:
                    print("Done! Press any key to continue")
                    with open(Sfile_path, "w") as f:
                        f.write(str(SReadlineDelay) + "\n")
                        f.write(str(SCustomLangPairs) + "\n")
                        f.write(str(file_path) + "\n")
                    key = readchar.readkey()
            elif choice2 == "4":
                file_pathUndo = file_path
                print("The Users tab fills automatically, start with \"/\" too, and write at the end \"/custom-lang.astro\" exactly, because the filepath is for a file, not a folder.")
                time.sleep(1)
                file_path = home_folder + input("\nEnter string/text: ")
                if not os.path.exists(file_path):
                    print("Path not found! Try write custom-lang.astro exactly, filepath not changed")
                    file_path = file_pathUndo
                else:
                    print("Done! Press any key to continue")
                    with open(Sfile_path, "w") as f:
                        f.write(str(SReadlineDelay) + "\n")
                        f.write(str(SCustomLangPairs) + "\n")
                        f.write(str(file_path) + "\n")
                    key = readchar.readkey()
            else:
                print(f"Typo: {choice2}\n2 Second pause")
                time.sleep(2)
    else:
        print(f"Typo: {choice1}\n2 Second pause")
        time.sleep(2)
