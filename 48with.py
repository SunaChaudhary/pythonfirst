#using with statement for file handling
with open("names.csv","r") as file:
    content=file.read()
    print(content)