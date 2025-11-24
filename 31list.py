#list used to stor multiple string type, integer type, mixed type data

names=['Sushma','Ram','Dhanraj']

print(names[0]) #we can print any index's value
print(names[1])
print(names[-1]) #printing last item

names[0]="Anita Chaudhary" #for replacing the value
print(names[0])

names.append("Sushma Chaudhary") #add item to the list
print(names)

names.remove("Ram") #remove item from the list
print(names)

print(len(names)) #find length of the list

names.reverse() #reverse the list
print(names)

