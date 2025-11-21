#number guess game which generates number from 1 to 6

import random
number=int(input("Enter a number 1-6:"))
cpunumber=random.randint(1,6)
print(f"cpunum={cpunumber}")
if number==cpunumber:
    print("Number matched")
else:
    print("Number not matched")