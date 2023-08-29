

# #Push:

books = []

books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")

print(books)


#Pop:

books.pop()
print(" The Last Book is : ",books[-1])

books.pop()
print(" The Last Book is : ",books[-1])

books.pop()
if not books:
    print("No books available")
