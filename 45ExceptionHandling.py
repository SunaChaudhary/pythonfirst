#Exception handling

try:
    num1= float(input("Enter num1:"))
    num2= float(input("Enter num2:"))
    sum=num1+num2
    print(f"Total is {sum}")
except:
    print("please enter only numbers")
finally:
    print("Program completed finally")
