import unittest
from .core import Book, Library

class TestSmartLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library("Test Library")
        self.book1 = Book("1984", "George Orwell", 328)
        self.book2 = Book("Dune", "Frank Herbert", 412)

    def test_book_dunder_methods(self):
        # Test __str__
        self.assertEqual(str(self.book1), "1984 by George Orwell")
        # Test __repr__
        self.assertIn("1984", repr(self.book1))
        # Test __len__
        self.assertEqual(len(self.book1), 328)
        # Test __eq__
        book1_duplicate = Book("1984", "George Orwell", 999)
        self.assertEqual(self.book1, book1_duplicate)
        self.assertNotEqual(self.book1, self.book2)

    def test_library_add_remove(self):
        # Test add_book (Admin)
        self.library.add_book(self.book1, role="Admin")
        self.assertEqual(len(self.library), 1)
        self.assertEqual(self.library[0], self.book1)

        # Test duplicate add
        with self.assertRaises(ValueError):
            self.library.add_book(self.book1, role="Admin")

        # Test remove_book (Admin)
        self.library.remove_book(self.book1, role="Admin")
        self.assertEqual(len(self.library), 0)

    def test_library_permissions(self):
        # Test add_book denial
        with self.assertRaises(PermissionError):
            self.library.add_book(self.book1, role="Guest")
        
        # Test remove_book denial
        self.library.add_book(self.book1, role="Admin")
        with self.assertRaises(PermissionError):
            self.library.remove_book(self.book1, role="Guest")

    def test_borrow_return(self):
        self.library.add_book(self.book1, role="Admin")
        
        # Test borrow
        self.library.borrow_item(self.book1, borrower="Alice")
        self.assertTrue(self.book1.is_borrowed)
        
        # Test double borrow
        with self.assertRaises(RuntimeError):
            self.library.borrow_item(self.book1, borrower="Bob")
            
        # Test return
        self.library.return_book(self.book1, borrower="Alice")
        self.assertFalse(self.book1.is_borrowed)
        
        # Test return not borrowed
        with self.assertRaises(RuntimeError):
            self.library.return_book(self.book1, borrower="Alice")

    def test_duck_typing(self):
        class MockItem:
            def __init__(self, title):
                self.title = title
        
        item = MockItem("Mock Magazine")
        # borrow_item uses duck typing for .title
        try:
            self.library.borrow_item(item, borrower="Carol")
        except Exception as e:
            self.fail(f"borrow_item failed with duck typing: {e}")

    def test_search(self):
        self.library.add_book(self.book1, role="Admin")
        self.library.add_book(self.book2, role="Admin")
        
        results = self.library.search("Orwell")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], self.book1)
        
        results = self.library.search("Dune")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], self.book2)

if __name__ == "__main__":
    unittest.main()
