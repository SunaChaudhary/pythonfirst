# simple way to create list

numbers=[x**2 for x in range(1,6)]
print(numbers)

#or
data={x :x**2 for x in range(1,6)}
print(data)

# for creating list of marks which are >8
scores=[65, 85, 90, 78, 88, 92, 56]
high_scores=[score for score in scores if score>80]
print("High score:", high_scores)

#or
student_scores={"Alice":85, "Bob":75, "David":90}
more_than_80={name:val for name, val in student_scores.items() if val>80}
print(more_than_80)

#for finding list of numbers that are divided by two
nums=[2,3,4,6,5,8]
divide_by_two=[num for num in nums if num%2==0]
print(divide_by_two)