# function to find cube of a number

def findcube():
    number= int(input("Enter a number:"))
    cube=number**3
    print(f"The cube of {number} is {cube}")

findcube()

#function that finds age from birth year

def findAge():
    current_year=2025
    birth_year=int(input("Enter your birth year:"))
    Age=current_year -birth_year
    print(f"Your age is: {Age}")

findAge()