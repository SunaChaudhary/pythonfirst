#finding average and total of expenses

expenses=[889,788,5656,4455,455,45]
total=0
n=0

for expense in expenses:
    total+=expense
    n+=1
    average=total/n
print(f"The average expenses is {average}")
print(f"Total sun of expenses is {total}")


