

class book:
    def __init__(self) :
        total_books=0
    @classmethod 
    def increment_book_count(cls): 
     cls.total_books += 1
book.increment_book_count() 
print(book.increment_book_count)    