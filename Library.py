class Library:
    def __init__(self, book_list):
        self.books = book_list  # List of available books
        self.lend_record = {}   # Dictionary to track borrowed books

    def display_books(self):
        print("\nAvailable Books:")
        if self.books:
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books available right now.")

    def lend_book(self, book_name, borrower):
        if book_name in self.books:
            self.books.remove(book_name)
            self.lend_record[book_name] = borrower
            print(f"\n'{book_name}' has been lent to {borrower}.")
        elif book_name in self.lend_record:
            print(f"\nSorry, '{book_name}' is already borrowed by {self.lend_record[book_name]}.")
        else:
            print(f"\nThe book '{book_name}' is not available in our library.")

    def return_book(self, book_name):
        if book_name in self.lend_record:
            self.books.append(book_name)
            self.lend_record.pop(book_name)
            print(f"\n'{book_name}' has been returned to the library.")
        else:
            print(f"\n'{book_name}' was not borrowed from this library.")

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"\n'{book_name}' has been added to the library.")

# Driver code to test the system
def main():
    library = Library(['Python Programming', 'Data Science with Python', 'Machine Learning Basics'])

    while True:
        print("\n\n--- Library Menu ---")
        print("1. Display Books")
        print("2. Lend Book")
        print("3. Return Book")
        print("4. Add Book")
        print("5. Exit")
        
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            library.display_books()
        elif choice == 2:
            book = input("Enter the book name you want to borrow: ")
            borrower = input("Enter your name: ")
            library.lend_book(book, borrower)
        elif choice == 3:
            book = input("Enter the book name you want to return: ")
            library.return_book(book)
        elif choice == 4:
            book = input("Enter the book name you want to add: ")
            library.add_book(book)
        elif choice == 5:
            print("Thank you for using the Library Management System!")
            break
            elif choice == 6:
            print("changed bruh1")
            break
            
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
