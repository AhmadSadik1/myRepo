from dateutil.relativedelta import *
from datetime import date
stop = False


def Age(dob):
    dobnew = tuple(map(int, dob.split(',')))
    age = relativedelta(date.today(), date(*dobnew))
    return age.years, age.months, age.days


def samllnum(number1, number2):
    if number1 < number2:
        return number1
    elif number2 < number1:
        return number2
    else:
        return "nono"


def stopiter(letter):
    global stop
    if letter == 'y':
        stop = True
    else:
        pass                                                                                                                            


while stop != True:
    name = input("Enter your name : ")
    birthday = input("Enter your birthday : ")
    print("Enter 2 number ")
    number1 = input("Enter the first number : ")
    number2 = input("Enter the secound number : ")
    print("Welcome sir")
    print(Age(birthday))
    print(samllnum(number1, number2))
    letter = input("Do want to exit [y|n] ")
    stopiter(letter)
