# import json 
# import os

# data_file = "library.txt"

# def load_library():
#  if os.path.exists(data_file):
#     with open(data_file , 'read') as file:
#      return json.load(file)   
#     return[]
    
#     def save_library(library):
#       with open(data_file , 'write') as file:
#         json.dump(library , file)
      
#     def add_book(library):
#       title = input("Enter the title of your book")
#       author = input("write author name")
#       year = input("year of your book?") 
#       generation = input("generation of your book")
#       read = input("Have you read the book ? (yes/no)").lower() == "yes" 


#       new_book = {
#           "title" : title,
#           "author": author,
#           "year":year,
#           "generation" :generation,
#           "read" :    read
#       }

#       library.append(new_book)
#       save_library(library)
#       print(f"Book {title} added successfully!")

#       def remove_book(library):
#         title = input("Enter the title of book")
#         initial_length = len(library)
#         library = [book for book in library if book["title"] != title]
#         if len(library) < initial_length:
#           save_library(library)
#           print(f"book {title} removed successfully")
#         else:
#           print(f"book {title} not found in library")

#         def search_library(library):
#           search_by = input("search by title").lower()
#           search_term = input(f"enter the {search_by} ").lower()

#           results = [book for book in library if search_term in book[search_by].lower()]



import json

class LibraryManager:
    def __init__(self):
        self.library = []
        self.file_name = 'library.json'

    def load_library(self):
        try:
            with open(self.file_name, 'r') as file:
                self.library = json.load(file)
        except FileNotFoundError:
            print("No previous library found. Starting with an empty library.")
            self.library = []

    def save_library(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.library, file)

    def add_book(self):
        print("Enter the book details:")

        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        year = input("Enter the publication year: ")
        while not year.isdigit():
            print("Please enter a valid number for the year.")
            year = input("Enter the publication year: ")
        year = int(year)

        genre = input("Enter the genre: ")
        read_status = input("Have you read this book? (yes/no): ").strip().lower()
        read_status = True if read_status == 'yes' else False

        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read_status
        }
        self.library.append(book)
        print(f"Book '{title}' added successfully!")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        book_found = False
        for book in self.library:
            if book['title'].lower() == title.lower():
                self.library.remove(book)
                print(f"Book '{title}' removed successfully!")
                book_found = True
                break

        if not book_found:
            print(f"No book found with the title '{title}'.")

    def search_book(self):
        print("Search by:")
        print("1. Title")
        print("2. Author")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title to search: ")
            found_books = [book for book in self.library if title.lower() in book['title'].lower()]
        elif choice == '2':
            author = input("Enter the author to search: ")
            found_books = [book for book in self.library if author.lower() in book['author'].lower()]
        else:
            print("Invalid choice!")
            return

        if found_books:
            print("\nMatching Books:")
            for idx, book in enumerate(found_books, start=1):
                print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
        else:
            print("No matching books found.")

    def display_books(self):
        if not self.library:
            print("Your library is empty.")
            return

        print("\nYour Library:")
        for idx, book in enumerate(self.library, start=1):
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

    def display_statistics(self):
        total_books = len(self.library)
        read_books = sum(1 for book in self.library if book['read'])
        percentage_read = (read_books / total_books) * 100 if total_books else 0

        print("\nLibrary Statistics:")
        print(f"Total books: {total_books}")
        print(f"Books read: {read_books}")
        print(f"Percentage read: {percentage_read:.2f}%")

    def show_menu(self):
        while True:
            print("\nMenu")
            print("Welcome to your Personal Library Manager!")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.search_book()
            elif choice == '4':
                self.display_books()
            elif choice == '5':
                self.display_statistics()
            elif choice == '6':
                self.save_library()
                print("Library saved to file. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

def main():
    library_manager = LibraryManager()
    library_manager.load_library()
    library_manager.show_menu()

if __name__ == "__main__":
    main()
