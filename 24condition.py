#condition in poython
#if, elif, else

age=int(input("Enter your age"))
print(f"You have entered your age {age}")

if age>=18:
    print("You are voter")
    print("you can vote")
else:
    print("you are not a voter")
    print("you can not vote")


#grade finding using coditions

percentage=int(input("Enter your percentage:"))
print(f"you have entered percentage is {percentage}")

if percentage>90:
    print("Your grade is A")
elif percentage>85 and percentage<=90:
    print("Your grade is A-")
elif percentage>80 and percentage<=85:
    print("Your grade is B+")
elif percentage>75 and percentage<=80:
    print("Your grade is B")
elif percentage>70 and percentage<=75:
    print("Your grade is B-")
elif percentage>65 and percentage<=70:
    print("Your grade is C+")
elif percentage>60 and percentage<=65:
    print("Your grade is C")
elif percentage>55 and percentage<=60:
    print("Your grade is C-")
elif percentage>50 and percentage<=55:
    print("Your grade is D+")
elif percentage>=45 and percentage<=50:
    print("Your grade is D")
else:
    print("Your grade is NG")