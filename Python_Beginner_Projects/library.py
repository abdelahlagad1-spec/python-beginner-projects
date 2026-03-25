class Library:
    books = []

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author, "available": True})
        print(f"Added '{title}' by {author}")

    def borrow_book(self, title):
        for book in self.books:
            if book["title"] == title:
                if book["available"]:
                    book["available"] = False
                    print(f"You borrowed '{title}'")
                    return
                else:
                    print(f"'{title}' not available")
                    return
        print(f"'{title}' not found")

    def return_book(self, title):
        for book in self.books:
            if book["title"] == title:
                book["available"] = True
                print(f"You returned '{title}'")
                return
        print(f"'{title}' not found")

library = Library()
library.add_book("1984", "George Orwell")
library.borrow_book("1984")
library.return_book("1984")
