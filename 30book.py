#searching book c
books=["Book A","Book B","Book C","Book D"]
for book in books:
    if book=="Book C":
        print("found Book C! stop searching")
        break
    print(f"Searching {books}")
print("Search ended")