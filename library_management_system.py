books = []
issuedbooks = []

def addbooks():
    name = input("Enter the name of the book: ")
    books.append(name)
    print("Book added")

def showbook():
    if len(books) == 0:
        print("No books are available")
    else:
        print("Available books:")
        for book in books:
            print(book)

def issuebook():
    showbook()
    name = input("Enter the name of the book to issue: ")
    
    if name in books:
        books.remove(name)
        issuedbooks.append(name)
        print("Book issued successfully")
    elif name in issuedbooks:
        print("Book is already issued")
    else:
        print("Book not available")

def returnbook():
    name = input("Enter the name of the book to return: ")
    
    if name in issuedbooks:
        issuedbooks.remove(name)
        books.append(name)
        print(name, "is returned")
    else:
        print("This book was not issued")

def library():
    while True:
        print("-" * 30)
        print("Menu")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        print("-" * 30)
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            addbooks()
        elif choice == 2:
            showbook()
        elif choice == 3:
            issuebook()
        elif choice == 4:
            returnbook()
        elif choice == 5:
            print("Thank you")
            break
        else:
            print("Invalid choice")

library()
