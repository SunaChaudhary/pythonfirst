#program to find a number is even or odd, even user enter a non-numeric value, handle exception and prompt user to enter a valid number

try:
    number=int(input("Enter a number:"))
    if number%2==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
except:
    print("Enter a valid number")
finally:
    print("Program completed finally")