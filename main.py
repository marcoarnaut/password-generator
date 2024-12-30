import math
import random
import os
import datetime

# const
eng_alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ru_alpha = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я", "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
spec_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+", "-", "\"", "'", ";", ":", "?" , "№", ">", "<"]
langs_count = 4
symb_count = len(eng_alpha) + len(ru_alpha) + len(numbers) + len(spec_symbols)
average_symbols = int((len(eng_alpha) + len(ru_alpha) + len(numbers) + len(spec_symbols))/langs_count)
avg_without_numbers_float = average_symbols-(average_symbols*(len(numbers)/symb_count))
tenth = str(avg_without_numbers_float)[(len(str(int(avg_without_numbers_float)))+1):][:1]
if int(tenth) > 4:
    avg_without_numbers = int(avg_without_numbers_float)+1
else:
    avg_without_numbers = int(avg_without_numbers_float)
numbers = numbers*(int(avg_without_numbers/len(numbers)))
entropy_values = ["very bad", "bad", "normal", "good", "very good"]

# functions

def func_dec(func: any) -> str:
    """Decorate return value"""
    def wrapped(*args: any) -> str:
        result = f'>>> {str(args).replace("(", "").replace(")", "")} {func.__name__}: {func(*args)}'
        return result
    return wrapped

def generatePassword(English_alphabet: str, Russian_alphabet: str, Numbers: str, Spec_Symbols: str, lenght: str, Copy: str) -> tuple:
    """Generate password with conditions"""
    try:
        chars = []
        if str(English_alphabet).lower() == "true" or str(English_alphabet).lower() == "t":
            chars = chars + eng_alpha
        if str(Russian_alphabet).lower == "true" or str(Russian_alphabet).lower == "t":
            chars = chars + ru_alpha
        if str(Numbers).lower() == "true" or str(Numbers).lower() == "t":
            chars = chars + numbers
        if str(Spec_Symbols).lower() == "true" or str(Spec_Symbols).lower() == "t":
            chars = chars + spec_symbols
        new_password = ""
        for i in range(int(lenght)):
            new_password += random.choice(chars)
        if str(Copy).lower() == "true" or str(Copy).lower() == "t":
            addToClipBoard(new_password)
        entropy = entropy_calc(new_password, len(chars))
        return new_password, entropy
    except:
        try:
            generatePassword("t", "t", "t", "t", lenght, "t")
        except:
            raise ValueError("Аргументы неправильно указаны!")

def entropy_calc(password: str, char_count: int) -> int:
    """Calculate an entropy of current password"""
    base = 2
    degree = len(str(password))
    number = char_count ** degree
    entropy = math.log(number, base)
    if entropy > 128:
        value = entropy_values[4]
    elif entropy > 60:
        value = entropy_values[3]
    elif entropy > 36:
        value = entropy_values[2]
    elif entropy > 28:
        value = entropy_values[1]
    else:
        value = entropy_values[0]
    entropy = value
    return entropy

def addToClipBoard(password: str) -> None:
    """Copy to clipboard with OS"""
    command = 'echo ' + password.strip() + '| clip'
    os.system(command)
    add_history(password)

def add_history(password: str) -> None:
    """Save as \'file password_history.txt\'"""
    try:
        now = str(datetime.datetime.now()).split(".")[0]
        file = open("password_history.txt", "r", encoding="utf-8")
        data = file.read()
        datasaves = data
        print(f"data: {data}")
        file.close()
        file = open("password_history.txt", "w", encoding="utf-8")
        print(datasaves)
        file.write(f"{datasaves}\n{now} - {password}\n")
    except:
        now = str(datetime.datetime.now()).split(".")[0]
        file = open("password_history.txt", "w", encoding="utf-8")
        file.write(f"{now} - {password}\n")
        print(f"data: +{password}")
    finally:
        file.close
# main
while True:
    inf = generatePassword(input("Enable ENG (True/False):"), input("Enable RU (True/False):"), input("Enable NUMS (True/False):"), input("Special Symbols (True/False): "), input("Lenght: "), input("Copy? (True/False): "))
    new_password = inf[0]
    entropy = inf[1]
    print(f"Generated Password: {new_password}\nEntropy: {entropy}")