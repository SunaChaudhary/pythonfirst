#No parameter and NO return type
def prime_minister():
    print("Current prime minister is Sushila Karki")

prime_minister()

#Parameter and no return type
def fullName(first_Name,last_Name):
    print(f"Full name is {first_Name} {last_Name}")

fullName("Suna","Chaudhary")

#No parameter and Return Type
def voter_age():
    return 18
ram_age=15

if ram_age>=voter_age():
    print("Ram is voter")
else:
    print("Ram is not voter")

#Parameter and Return Type
def full_Name(first_Name,last_Name):
    fullname=f"{first_Name} {last_Name}"
    return fullname

fn=full_Name("Dharnraj","Woad")
print(fn)