class Library:
    def __init__(self):
        # we list all the books here, its Title and availablity
        self.books = [
            {"Title": "Master Python in 2 hours", "is_available":True},
             {"Title": "Coding is fun and simple", "is_available":True},
              {"Title": "Object oriented programming", "is_available":False},
               {"Title": "Master Java", "is_available":True},
                {"Title": "Algorithm in Python", "is_available":False},
            ]
    def view_books(self): # this function we call them whenever we want to view our books
            print('\n All available books:')
            for index,element in enumerate(self.books, start = 1): # we organize our list of books, the index is by default zero, to make it readable, we start at 1
                status = "available" if element["is_available"] else "Not available" # very classic pythonic oneliner, I must adnit i looked online on how to shortern the line
                print(f"{index} {element['Title']} : {status}") # we print the index , the book title and available
        
                
    def borrow_book(self,book_num):
        if 0 < book_num <= len(self.books):# Check if the book number is within the valid range
            book = self.books[book_num - 1]# Get the book from the list (adjusting for 0-based index)
            if  book["is_available"]: #check if a book is available
                book["is_available"] = False # if yes then check as borrowed
                print(f'{book["Title"]} have been successful borrowed.') # sucessful message
            else:
                print(f'the {book["Title"]} is not available at the moment') 
        else: 
                print('Invalid book num')
            
    def return_book(self,book_num):
        if 0 < book_num <=len(self.books):# Check if the book number is within the valid range
            book = self.books[book_num - 1]# Get the book from the list (adjusting for 0-based index)
            if not  book["is_available"]:# Check if the book is currently not available (borrowed)
                book["is_available"] = True # Mark the book as available
                print(f'{book["Title"]} have been successful returned.') # Print a success message
            else:
                print(f'"{book["Title"]}" was not borrowed, so it cannot be returned.') # Print a message indicating the book was not borrowed

        else:
            print('Invalid books')# Print a message indicating the book number is invalid         


    def welcome(self):
       print("Welcome to the Library Management System!")
       print("1: View available books")
       print('2:Borrow a book')
       print('3: Return a book')
       print('4: Exit')

   
  

    def runSoftware(self): #created a loading app function
        while True:
            self.welcome() # first it shows a welcome message

            choice = input("Enter your choice: ") # we ask user for input an integer
            if choice == "1":
                self.view_books() # if user input 1, we load the view book function
            elif choice == "2":
                self.view_books() # even though user didnt ask for to view books, we loaded for a user to pick
                try: #error handling in case user put a number thats not contain  in our book lisr
                    book_num = int(input("Enter the book number to borrow: "))
                    self.borrow_book(book_num)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "3":
                self.view_books()
                try:
                    book_num = int(input("Enter the book number to return: "))
                    self.return_book(book_num)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "4":
                print("Thank you for using the library system!")
                break
            else:
                print("Invalid choice, please try again.")




library = Library()
library.runSoftware()