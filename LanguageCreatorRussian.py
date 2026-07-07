import os
import readchar
import time
SReadlineDelay = 0.3
SCustomLangPairs = 50                       # 33 буквы + 10 цифр + 7 знаков
home_folder = os.path.expanduser("~")
file_path = home_folder + "/Desktop/custom-lang-rus.astro"
Sfile_path = home_folder + "/Documents/Misc-rus.astro"

# Загрузка или создание файла настроек
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
    Добро пожаловать в: 
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
    🟩🟩🟩\033[1m\033[32m&#$* > Джон\033[32m\033[1m🟩🟩🟩
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
    🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩

    СОЗДАТЕЛЬ СЕКРЕТНОГО ЯЗЫКА
     \033[0mОт \033[95mAstroVoid24""")
    choice1 = input("""\033[0mЧто вы хотите сделать?
        ПОЛЬЗОВАТЕЛЬСКИЙ ЯЗЫК → Русский - \"1\"
        Русский → ПОЛЬЗОВАТЕЛЬСКИЙ ЯЗЫК - \"2\"
        СОЗДАТЬ ПОЛЬЗОВАТЕЛЬСКИЙ ЯЗЫК - \"3\"
        Автоматическое создание (Не рекомендуется!) - \"4\"
        Список пар - \"5\"
        Настройки (будет пополняться) - \"6\"
        Ответ: """)

    if choice1 == "3":
        FullLanguage = []
        print(f"""Инструкция:
        Введите символ вашего языка, а затем русскую букву
        и нажмите Enter для перехода к следующей букве.
        Пример: &а *Нажать Enter*
                 %б *Нажать Enter*
        Требуется {SCustomLangPairs} пар, но в алфавите всего 33 буквы?
        Верно, но есть и другие важные символы, а главное – ЦИФРЫ!
        Дополнительные символы: 1234567890,.=+-%?
        Не используйте \\q, это сломает программу.
        Рекомендуется вводить русские буквы по алфавиту, затем цифры, затем остальные символы.
        Чтобы отправить язык другу, передайте ему файл \"custom-lang-rus.astro\" с рабочего стола,
        он должен поместить его на свой рабочий стол.""")
        for LineLetter in range(SCustomLangPairs):
            pair = input(f"Доп. символы: 1234567890,.=+-%? | Пара {LineLetter + 1}:")
            FullLanguage.append(pair)
        with open(file_path, "w") as f:
            for pair in FullLanguage:
                f.write(pair + "\n")
        with open(file_path, "r") as file:
            Review = file.read()
            print("Всё готово!\nПроверьте свой перевод!:")
            time.sleep(1)
            print(Review + "\nНажмите любую клавишу для продолжения")
            key = readchar.readkey()

    elif choice1 == "4":
        with open(file_path, "w") as f:
            f.write("""!а
@б
#в
$г
%д
^е
&ё
*ж
(з
)и
_й
-к
+л
=м
[н
]о
{п
}р
|с
:т
;у
'ф
\"х
<ц
>ч
.ш
,щ
/ъ
\\ы
`ь
~э
@ю
#я
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
Q?""")
        print("Готово! Нажмите любую клавишу для продолжения")
        key = readchar.readkey()

    elif choice1 == "2":
        if not os.path.exists(file_path):
            print("Файл языка не найден. Сначала создайте его (пункты 3 или 4).")
            time.sleep(2)
        else:
            Translation = {}
            with open(file_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        symbol = line[:-1]
                        letter = line[-1]
                        Translation[letter] = symbol

            FromRussian = input("Текст (русский): ")
            result = ""
            for char in FromRussian:
                if char in Translation:
                    result += Translation[char]
                else:
                    print("Не буду переводить! Не смог найти одну из букв, попробуйте писать строчными буквами, хорошо? Я не буду продолжать,\nпотому что если я продолжу, вы сможете прочитать всё целиком, просто без одного или двух букв и\nя не знаю, кто за этим компьютером!")
                    result = ""
                    break
            print(f"{FromRussian} -> {result}\nНажмите любую клавишу для продолжения")
            key = readchar.readkey()

    elif choice1 == "1":
        if not os.path.exists(file_path):
            print("Файл языка не найден. Сначала создайте его (пункты 3 или 4).")
            time.sleep(2)
        else:
            TranslationToRus = {}
            with open(file_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        symbol = line[:-1]
                        letter = line[-1]
                        TranslationToRus[symbol] = letter

            ToRussian = input("Текст (на секретном языке): ")
            result = ""
            for char in ToRussian:
                if char in TranslationToRus:
                    result += TranslationToRus[char]
                else:
                    print("Не буду переводить! Не смог найти одну из букв, попробуйте писать строчными буквами, хорошо? Я не буду продолжать,\nпотому что если я продолжу, вы сможете прочитать всё целиком, просто без одного или двух букв и\nя не знаю, кто за этим компьютером!")
                    result = ""
                    break
            print(f"{ToRussian} -> {result}\nНажмите любую клавишу для продолжения")
            key = readchar.readkey()

    elif choice1 == "5":
        if not os.path.exists(file_path):
            print("Файл языка не найден. Сначала создайте его (пункты 3 или 4).")
            time.sleep(2)
        else:
            print("Текущие пары:")
            time.sleep(1)
            with open(file_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        print(line)
                        time.sleep(SReadlineDelay)
            print("Нажмите любую клавишу для продолжения")
            key = readchar.readkey()

    elif choice1 == "6":
        SExit = True
        while SExit:
            print("\n" * 100)
            print("""⚙ Настройки ⚙
    1 - Выход
    2 - Задержка вывода пар (число)
    3 - Количество пользовательских пар (число)
    4 - Путь к файлу custom-lang-rus.astro (текст)""")
            choice2 = input("Введите ваш выбор: ")
            if choice2 == "1":
                SExit = False
            elif choice2 == "2":
                try:
                    SReadlineDelay = int(float(input("\nВведите целое/число: ")))
                except ValueError:
                    print("Обнаружена строка, значение не изменено. Нажмите любую клавишу для продолжения")
                    key = readchar.readkey()
                else:
                    print("Готово! Нажмите любую клавишу для продолжения")
                    with open(Sfile_path, "w") as f:
                        f.write(str(SReadlineDelay) + "\n")
                        f.write(str(SCustomLangPairs) + "\n")
                        f.write(str(file_path) + "\n")
                    key = readchar.readkey()
            elif choice2 == "3":
                try:
                    SCustomLangPairs = int(float(input("\nВведите целое/число: ")))
                except ValueError:
                    print("Обнаружена строка, значение не изменено. Нажмите любую клавишу для продолжения")
                    key = readchar.readkey()
                else:
                    print("Готово! Нажмите любую клавишу для продолжения")
                    with open(Sfile_path, "w") as f:
                        f.write(str(SReadlineDelay) + "\n")
                        f.write(str(SCustomLangPairs) + "\n")
                        f.write(str(file_path) + "\n")
                    key = readchar.readkey()
            elif choice2 == "4":
                file_pathUndo = file_path
                print("Путь начинается от домашней папки, начните с \"/\" и в конце укажите \"/custom-lang-rus.astro\", потому что это путь к файлу, а не к папке.")
                time.sleep(1)
                file_path = home_folder + input("\nВведите строку/текст: ")
                if not os.path.exists(file_path):
                    print("Путь не найден! Введите точно custom-lang-rus.astro, путь не изменён")
                    file_path = file_pathUndo
                else:
                    print("Готово! Нажмите любую клавишу для продолжения")
                    with open(Sfile_path, "w") as f:
                        f.write(str(SReadlineDelay) + "\n")
                        f.write(str(SCustomLangPairs) + "\n")
                        f.write(str(file_path) + "\n")
                    key = readchar.readkey()
            else:
                print(f"Опечатка: {choice2}\n2-секундная пауза")
                time.sleep(2)
    else:
        print(f"Опечатка: {choice1}\n2-секундная пауза")
        time.sleep(2)