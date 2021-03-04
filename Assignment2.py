import os
import os
clear = lambda: os.system('cls')
clear()

def ext():
    exit


def retir():
    print("  ")
    print("You have selected to Calculate retirement")
    print("  \n  ")

    age = input("Please enter your age: ")
    annualSal = input("Please enter you annual salary: ")
    percentsave = input("Please enter percentage saved(please only input the number do not include the (%)): ")
    desiredsavinggoal = input("Plase enter your desiered retirement saving goal: ")

    age = (int(age))
    annualSal = (int(annualSal))
    percentsave = (int(percentsave))
    desiredsavinggoal = (int(desiredsavinggoal))
    

    menu()
    return


def bmical():
    print("  ")
    print("You have selected to Calculate Body Mass Index: ")
    print("  \n  ")
    
    heightfeet = input("Please enter your height in feet: ")
    heightinches = input("Please enter your height in inches: ")
    heightweight = input("Please enter your weight in pounds: ")

    heightfeet = (int(heightfeet))
    heightinches = (int(heightinches))
    heightweight = (int(heightweight))

    nw = heightweight * 0.45
    ni = heightfeet * 12
    nh = (ni + heightinches) * 0.025
    nh2 = nh * nh
    answer = nw / nh2

    if answer < 18.5:
        category = ("Underweight ")
        
    
    if answer >= 18.5 and answer <= 24.9:
        category = ("Normal weight")
    
    if answer  >= 25 and answer <= 29.9:
        category = ("Overweight ")
    
    if answer >= 30:
        category = ("Obese")

    print("Your BMI calculation is: ", answer)
    print("Your category is: ", category)
    print("  \n   \n   ")

    menu()


def menu():
    print("Welcome to the Menu \n 1. Calculate Body Mass Index \n 2. Calculate Retierment \n 3. Exit Program")
    a = input("Which option would you like to select: ")
    print(a)
    while a != "1" or a != "2" or a != "3":
        if a == "1":
            bmical()
            return
        if a == "2":
            retir()
            return
        if a == "3":
            ext()
            return
        if   a != "1" or a != "2" or a != "3":
            print("  ")
            a = input(" You entered a incorrect number \n Please enter 1, 2, or 3 :")
    
menu()

