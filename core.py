"""
core.py – Book and Library classes for the Smart Library System.

Dunder methods implemented:
    Book:    __str__, __repr__, __len__, __eq__
    Library: __str__, __len__, __getitem__ (makes Library iterable)
"""

from __future__ import annotations

from .utils import permission_check, track_access


class Book:
    
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self._is_borrowed: bool = False

    def __str__(self) -> str:
        """Return a user-friendly string: 'Title by Author'."""
        return f"{self.title} by {self.author}"

    def __repr__(self) -> str:
        """Return an unambiguous developer representation."""
        return (
            f"Book(title={self.title!r}, author={self.author!r}, "
            f"pages={self.pages!r})"
        )

    def __len__(self) -> int:
        """Return the number of pages in the book."""
        return self.pages

    def __eq__(self, other: object) -> bool:
        """Two books are equal if they share the same title and author."""
        if not isinstance(other, Book):
            return NotImplemented
        return (
            self.title.lower() == other.title.lower()
            and self.author.lower() == other.author.lower()
        )

    @property
    def is_borrowed(self) -> bool:
        """Whether the book is currently checked out."""
        return self._is_borrowed


class Library:
   
    def __init__(self, name: str) -> None:
        self.name = name
        self._books: list[Book] = []


    def __str__(self) -> str:
        return f"Library('{self.name}', {len(self._books)} book(s))"

    def __repr__(self) -> str:
        return f"Library(name={self.name!r})"

    def __len__(self) -> int:
        """Return the number of books currently in the library."""
        return len(self._books)

    def __getitem__(self, index: int) -> Book:
       
        return self._books[index]


    @permission_check("Admin")
    def add_book(self, book: Book, *, role: str = "Guest") -> None:
        if book in self._books:
            raise ValueError(f"'{book}' is already in the library.")
        self._books.append(book)
        print(f"  [+] Added: {book}")

    def remove_book(self, book: Book, *, role: str = "Guest") -> None:

        # Inline permission check to demonstrate the closure separately
        if role != "Admin":
            raise PermissionError(
                f"Access denied: 'remove_book' requires role 'Admin', "
                f"but got '{role}'."
            )
        if book not in self._books:
            raise ValueError(f"'{book}' not found in the library.")
        self._books.remove(book)
        print(f"  [-] Removed: {book}")

    @track_access
    def borrow_item(self, item: object, *, borrower: str = "Anonymous") -> None:
        
        # Duck typing: access .title without checking the type
        title = item.title  # noqa: raises AttributeError if missing

        # If it's a Book, track its borrow status
        if hasattr(item, "_is_borrowed"):
            if item._is_borrowed:
                raise RuntimeError(f"'{title}' is already borrowed.")
            item._is_borrowed = True

        print(f"  [->] '{title}' borrowed by {borrower}.")

    @track_access
    def return_book(self, book: Book, *, borrower: str = "Anonymous") -> None:
        
        if not book._is_borrowed:
            raise RuntimeError(f"'{book.title}' was not borrowed.")
        book._is_borrowed = False
        print(f"  [<-] '{book.title}' returned by {borrower}.")

    def search(self, query: str) -> list[Book]:
        
        q = query.lower()
        return [
            b for b in self._books if q in b.title.lower() or q in b.author.lower()
        ]
