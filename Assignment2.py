import os
import math
clear = lambda: os.system('cls')
clear()


def ext():
    quit()
        
def retir(age,annualSal,percentsave,desiredsavinggoal):

    savPerYear = (annualSal * percentsave) * 1.35
    numYear = desiredsavinggoal / savPerYear
    CompletionAge = age + numYear

    CompletionAge = math.ceil(CompletionAge)

    if CompletionAge >= 100:
        CompletionAge = 0

    return (CompletionAge)

def bmical(heightfeet,heightinches,heightweight):   

    nw = heightweight * 0.45
    ni = heightfeet * 12
    nh = (ni + heightinches) * 0.025
    nh2 = nh * nh
    answer = nw / nh2

    if answer < 18.5:
        category = ("Underweight")       
    
    if answer >= 18.5 and answer <= 24.9:
        category = ("Normal weight")
    
    if answer >= 25 and answer <= 29.9:
        category = ("Overweight") 

    if answer >= 30:
        category = ("Obese")

    answer = round(answer)

    return (answer, category)


def menu():
    print("Welcome to the Menu \n 1. Calculate Body Mass Index \n 2. Calculate Retierment \n 3. Exit Program")
    selection = input("Which option would you like to select: ")
    a = selection
    while a != "1" or a != "2" or a != "3":
        if a == "1":
            print("  ")
            print("You have selected to Calculate Body Mass Index: ")
            print("  \n  ")

            heightfeet = input("Please enter your height in feet: ")
            heightinches = input("Please enter your height in inches: ")
            heightweight = input("Please enter your weight in pounds: ")

            heightfeet = (int(heightfeet))
            heightinches = (int(heightinches))
            heightweight = (int(heightweight))

            answer, category = bmical(heightfeet,heightinches,heightweight)

            print("Your BMI calculation is: ", round(answer))
            print("Your category is: ", category)
            print("  \n   \n   ")

            menu()

        if a == "2":
            print("  ")
            print("You have selected to Calculate retirement")
            print("  \n  ")

            age = input("Please enter your age: ")
            annualSal = input("Please enter you annual salary: ")
            percentsave = input("Please enter percentage saved as a decimel: ")
            desiredsavinggoal = input("Plase enter your desiered retirement saving goal: ")

            age = (int(age))
            annualSal = (int(annualSal))
            percentsave = (float(percentsave))
            desiredsavinggoal = (int(desiredsavinggoal))

            CompletionAge = retir(age,annualSal,percentsave,desiredsavinggoal)

            if CompletionAge == 0:
                print("   ")
                print("Saving Goal cannot be met before age 100")
                print("  \n  ")
                menu()

            print("You can reitre at this age with the desiered goal: ", CompletionAge)
            print("  \n  ")
            menu()

        if a == "3":
            print("  ")
            print(" Exciting Application... ")
            print("  ")
            ext()        

        if   a != "1" or a != "2" or a != "3":
            print("  ")
            a = input(" You entered a incorrect number \n Please enter 1, 2, or 3 :")


menu()
#For some reason the Test will not run when menu is called even though I do not test menu
#and the funcitons mention do not call menu at any point, I apoglize for the error but 
#I cannot seem to find a solution