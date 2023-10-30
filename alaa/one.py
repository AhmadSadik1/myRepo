import datetime as dt


number = int(input("Enter number of student "))

for i in range(number):
    name = input('Enter your name : ')
    age = int(input("Enter your age "))
    num1 = int(input("num1 : "))
    num2 = int(input("num2 : "))
    current_year = dt.datetime.year()
    z = current_year - age
    min_number = min(num1, num2)
    print(f"Welocme {name} , age{z}")
    w = input("Age you exit? [y|n]")
    if w == 'y':
        break
    else:
        continue
