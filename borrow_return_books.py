"""
1.Store the titles, authors, and statuses (available or borrowed) of 5 books in a list.
2.Allow users to borrow or return books.
3.Print the updated book information after each transaction.
4.Prevent users from borrowing a book that is already borrowed.
5.Keep track of the number of times each book has been borrowed.

enumerate:-
It helps count things in a list and tells you both the number (index) and the item at the same time.

"""

book_list = [{"title": "Brave New World", "author": "Aldous Huxley", "borrow_count": 0},
             {"title": "The Devil Wears Prada", "author": "Lauren Weisberger", "borrow_count": 0},
             {"title": "Jane Eyre", "author": "Charlotte Brontë", "borrow_count": 0},
             {"title": "Pride and Prejudice", "author": "Jane Austen", "borrow_count": 0},
             {"title": "To Kill a Mockingbird", "author": "Harper Lee", "borrow_count": 0}]

def book_names():
    for num, book in enumerate(book_list):
        # print(f"1 = {books[0]['title']} ")
        print(f"{num} = {book['title']}")


def borrow_or_return():
    print("1 = borrow a book ")
    print("2 = return a book")
    borrow_or_return_books = int(input("do you want to borrow or return books:  "))

    if borrow_or_return_books == 1:
        book_names()
        borrow_book_name = int(input("Which book do you want to borrow:  "))

        if book_list[borrow_book_name]["borrow_count"] == 1:
            print("The book has been borrowed by someone")

        else:
            book_list[borrow_book_name]["borrow_count"] += 1
            print("The book has been successfully borrowed by you")

    elif borrow_or_return_books == 2:
        book_names()
        return_book_name = int(input("Which book do you want to return:  "))
        book_list[return_book_name]["borrow_count"] -= 1
        print("The book has been successfully returned")

    else:
        print("Please enter a valid number")

borrow_or_return()
