# total and average skip zero value and stop negative value
values=[10,0,25,0,50,-1,40]
total=0
n=0

for v in values:
    if v==0:
        continue
    if v<0:
        break
    total+=v
    n+=1
    average=total/n
print(f"total is {total}")
print(f"average is {average}")