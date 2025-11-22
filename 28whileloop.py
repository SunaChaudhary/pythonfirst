#while loop

num=1

while num<=100:
    print(num)
    num+=1


#countdown timer using while loop

countdown=10

while countdown>0:
    print(f"the countdown is:{countdown}")
    countdown-=1
print("The countdown is completed")

#password grant

password="" 
while password !="1234@#":
    password=input("Enter the password:")
print("Access granted")