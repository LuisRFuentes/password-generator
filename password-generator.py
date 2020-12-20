# Password Generator
# Project made for the course "Python Basic Course" in Platzi
# Made by: LuisRFuentes

import random


def generate_password(use_mayus, use_minus, use_numbers, use_simbols, pass_length):
    MAYUS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    MINUS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    SIMBOLS = ('/', '*', '-', '_', '@', '&', '%', '!')
    combination = []
    if use_mayus:
        combination += MAYUS
    if use_minus:
        combination += MINUS
    if use_numbers:
        combination += NUMBERS
    if use_simbols:
        combination += SIMBOLS
    password = ""
    i = 0
    while i < pass_length:
        password += random.choice(combination)
        i += 1
    return password


def get_use(type):
    resp = input("Use " + type + "?" + "(y/n): ")
    while resp != 'y' and resp != 'n' and resp != 'Y' and resp != 'N':
        resp = input("Wrong answer, please indicate your answer with a 'y' (yes) or a 'n' (no): ")
    if resp.lower() == 'y':
        return True
    else:
        return False


def main():
    mayus = get_use("mayus")
    minus = get_use("minus")
    numbers = get_use("numbers")
    simbols = get_use("simbols")
    if mayus or minus or numbers or simbols:
        pass_length = int(input("How many characters will be in the password? (min length: 6 characters): "))
        while pass_length < 6:
            pass_length = int(input("Please, indicate a mayor length: "))
        password = generate_password(mayus, minus, numbers, simbols, pass_length)
        print("Your new password is: " + password)
    else:
        print("Can't generate password without any caracter :(")


if __name__ == '__main__':
    main()