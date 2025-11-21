import random
print(random.random())

#for specific range
randomnum=random.randint(1,10)
print(randomnum)

#for random name from a list
names=["Suna","Sushma","Ram","Dhanraj"]
random.shuffle(names)
print(names[0])