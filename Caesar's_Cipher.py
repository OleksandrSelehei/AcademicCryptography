Alphabet_EU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Alphabet_UA = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"


def encription_eu(txt, k):
    result = ""
    text = txt.upper()
    for item in text:
        if item != " ":
            new_index = Alphabet_EU.index(item) + k
            if new_index > 25:
                new_index = new_index - 25
            result = result + Alphabet_EU[new_index]
        else:
            result = result + '_'
    return result


def decription_eu(txt, k):
    result = ""
    text = txt.upper()
    for item in text:
        if item != "_":
            new_index = Alphabet_EU.index(item) - k

            if new_index < 0:
                new_index = 25 + new_index
            result = result + Alphabet_EU[new_index]
        else:
            result = result + ' '
    return result

def encription_ua(txt, k):
    result = ""
    text = txt.upper()
    for item in text:
        if item != " ":
            new_index = Alphabet_UA.index(item) + k
            if new_index > 32:
                new_index = new_index - 32
            result = result + Alphabet_UA[new_index]
        else:
            result = result + '_'
    return result


def decription_ua(txt, k):
    result = ""
    text = txt.upper()
    for item in text:
        if item != "_":
            new_index = Alphabet_UA.index(item) - k
            if new_index < 0:
                new_index = 32 + new_index
            result = result + Alphabet_UA[new_index]
        else:
            result = result + ' '
    return result


def atak_eu(txt):
    text = txt.upper()
    for k in range(25):
        result = ""
        for item in text:
            if item != "_":
                new_index = Alphabet_EU.index(item) - k
                if new_index < 0:
                    new_index = 25 + new_index
                result = result + Alphabet_EU[new_index]
            else:
                result = result + ' '
        print(result)


def atak_ua(txt):
    text = txt.upper()
    for k in range(32):
        result = ""
        for item in text:
            if item != "_":
                new_index = Alphabet_UA.index(item) - k
                if new_index < 0:
                    new_index = 32 + new_index
                result = result + Alphabet_UA[new_index]
            else:
                result = result + ' '
        print(result)

#INTERFICE#
boolian = True
while boolian:
    leng = input("Оберіть мову/Choose a language(UA/EU): ")
    if leng == "UA":
        func = input("Оберіть дію(Шифрування/Дешифрування/Атака): ")
        if func == "Шифрування":
            txt = input("Введіть текст: ")
            k = int(input("Введіть ключ: "))
            print(encription_ua(txt, k))
            boolian_text = input("Вийти(так/ні): ")
            if boolian_text == "так":
                boolian = False
            else:
                boolian = True
        elif func == "Атака":
            txt = input("Введіть текст: ")
            print(atak_ua(txt))
            boolian_text = input("Вийти(так/ні): ")
            if boolian_text == "так":
                boolian = False
            else:
                boolian = True
        else:
            txt = input("Введіть текст: ")
            k = int(input("Введіть ключ: "))
            print(decription_ua(txt, k))
            boolian_text = input("Вийти(так/ні): ")
            if boolian_text == "так":
                boolian = False
            else:
                boolian = True
    else:
        func = input("Choose an action (Encrypt/Decrypt/Attack): ")
        if func == "Encrypt":
            txt = input("Enter the text:")
            k = int(input("Enter the key:"))
            print(encription_eu(txt, k))
            boolian_text = input("EXIT(yes/no): ")
            if boolian_text == "yes":
                boolian = False
            else:
                boolian = True
        elif func == "Attack":
            txt = input("Enter the text:")
            print(atak_eu(txt))
            boolian_text = input("EXIT(yes/no): ")
            if boolian_text == "yes":
                boolian = False
            else:
                boolian = True
        else:
            txt = input("Enter the text:")
            k = int(input("Enter the key:"))
            print(decription_eu(txt, k))
            boolian_text = input("EXIT(yes/no): ")
            if boolian_text == "yes":
                boolian = False
            else:
                boolian = True