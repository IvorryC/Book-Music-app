from typing import List # , Tuple, Set, etc

class Book:
    pass

class Bookshelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books"