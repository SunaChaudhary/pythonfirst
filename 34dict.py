#dictionary in python
datas={'Nepal':'Kathmandu', "India":"New Delhi", "US":"WDC"}

print(f"Capital city of Nepal is {datas['Nepal']} ")

datas["Nepal"]="KTM" #replacement
print(f"Capital city of Nepal is {datas['Nepal']} ")

datas["Japan"]='Tokiyo' #to add a key value pair in a dictionary
print(f"Capital city of Japan is {datas['Japan']}")

datas.pop("US") #to remove key value pair from dictionary
print(datas)

print('China' in datas) #to check the given key is exist in dictionary or not
print('Nepal' in datas)
