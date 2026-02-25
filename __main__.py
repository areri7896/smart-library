
from . import Book, Library


def section(title: str) -> None:
    """Print a formatted section header using plain ASCII."""
    bar = "-" * 60
    print(f"\n{bar}")
    print(f"  {title}")
    print(bar)


def main() -> None:
    print("=" * 60)
    print("   [*] Smart Library System  --  Demo")
    print("=" * 60)

    section("1. Creating Library & Adding Books (Admin Only)")

    lib = Library("Newbies Public Library")
    print(f"  Library created: {lib}")

    books = [
        Book("1984", "George Orwell", 328),
        Book("Dune", "Frank Herbert", 412),
        Book("The Alchemist", "Paulo Coelho", 208),
        Book("Things Fall Apart", "Chinua Achebe", 209),
        Book("Atomic Habits", "James Clear", 320),
    ]

    for book in books:
        lib.add_book(book, role="Admin")

    print(f"\n  Total books in library: {len(lib)}")

   

    for book in lib:
        print(f"  - {book}  |  pages={len(book)}")

    section("3. Dunder Methods: __str__, __len__, __eq__")

    b1 = Book("1984", "George Orwell", 328)
    b2 = Book("1984", "George Orwell", 999)  # same title+author, different pages
    b3 = Book("Dune", "Frank Herbert", 412)

    print(f"  str(b1)  -> {b1}")
    print(f"  len(b1)  -> {len(b1)} pages")
    print(f"  b1 == b2 -> {b1 == b2}  (same title & author, pages ignored)")
    print(f"  b1 == b3 -> {b1 == b3}  (different book)")

    # ------------------------------------------------------------------ #
    # 4. Borrow & Return (@track_access decorator)
    # ------------------------------------------------------------------ #
    section("4. Borrowing & Returning Books  (@track_access logs above)")

    target = lib[0]  # Book at index 0 via __getitem__
    lib.borrow_item(target, borrower="Alice")
    lib.return_book(target, borrower="Alice")

    # Borrow again to show another log entry
    lib.borrow_item(target, borrower="Bob")

    section("5. Duck Typing:  borrow_item() on a non-Book object")

    class Magazine:
        """A magazine -- NOT a Book, but has a .title attribute."""

        def __init__(self, title: str, issue: int) -> None:
            self.title = title
            self.issue = issue

    vogue = Magazine("Vogue Africa", issue=42)
    print("  Passing a Magazine (not a Book) to borrow_item ...")
    lib.borrow_item(vogue, borrower="Carol")
    print("  [OK] Works seamlessly -- Duck Typing confirmed.")

  
    section("6. Access Control:  permission_check('Admin')")

    new_book = Book("Python Tricks", "Dan Bader", 302)
    print("  Attempting to add a book with role='Guest' ...")
    try:
        lib.add_book(new_book, role="Guest")
    except PermissionError as exc:
        print(f"  [OK] PermissionError raised -> {exc}")

    print("\n  Adding the same book with role='Admin' ...")
    lib.add_book(new_book, role="Admin")
    print(f"  Library now has {len(lib)} books.")

   
    section("7. Search")

    results = lib.search("orwell")
    print(f"  Search 'orwell' -> {[str(b) for b in results]}")

    results2 = lib.search("atomic")
    print(f"  Search 'atomic' -> {[str(b) for b in results2]}")

    
    section("Demo Complete")
    print(f"  Final state: {lib}")
    print()


if __name__ == "__main__":
    main()
