#set
fruits={"Apple","Orange","Banana","Apple"}

print(fruits)

fruits.add("Papaya") # for adding item
print(fruits)

fruits.remove("Orange") #for removing item
print(fruits)

for fruit in fruits:
    print(fruit) # for printing fruit from set one by one

#inse_rtion for common items
course_A_student={"Alice","Bob","Ram"}
course_B_student={"Alice","Bob", "Charlie"}
common_course_student= course_A_student.intersection(course_B_student)
print(common_course_student)