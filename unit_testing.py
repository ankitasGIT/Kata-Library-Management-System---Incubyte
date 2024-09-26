from library_operations import Book, Library

class TestLibraryManagementSystem:
    def init(self):
        self.library = None
        self.book = None

    def setUp(self):
        self.library = Library()
        self.library.clear_all_data()

        self.book = Book("6", "Test Book", "Test Author", 2023)
        self.library.add_book(self.book)

    """ Testing check for add_book() """
    def test_add_book(self):
        assert self.book.isbn in self.library.books, f"AssertionError: {f'{self.book.isbn} not found in {self.library.books}'}"

    """Testing check for borrow book() """
    def test_borrow_book(self):
        self.library.borrow_book(self.book.isbn)
        assert not self.library.books[self.book.isbn].is_available, f"AssertionError: {'Expected False, but got True'}"

    def test_borrow_unavailable_book(self):
        try:
            self.library.borrow_book(self.book.isbn)
            raise AssertionError(f"AssertionError: Unavailable book borrowed")
        except:
            return True

def run_tests():
    test_suite = TestLibraryManagementSystem()
    """ Fetching all methods for unit testing  """
    test_methods = [method for method in dir(test_suite) if method.startswith('test_')]
    
    
    for method in test_methods:
        test_suite.setUp()
        try:
            getattr(test_suite, method)()
            print(f"{method} - PASS")
        except AssertionError as e:
            print(f"{method} - FAIL: {str(e)}")
        except Exception as e:
            print(f"{method} - ERROR: {str(e)}")

if __name__ == '__main__':
    run_tests()
