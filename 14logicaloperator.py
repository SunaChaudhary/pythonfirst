#logical operator

atm_user_id=10
user_pin=1020

inputid=int(input("Enter your user id:"))
inputpin=int(input("Enter pin:"))

if atm_user_id==inputid and user_pin==inputpin:
 print("Login successfully")
else:
 print("Login failed")