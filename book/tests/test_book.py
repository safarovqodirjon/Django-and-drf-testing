from django.test import TestCase
from django.db.utils import IntegrityError
from book.models import Author, Book

class BookModelTest(TestCase):
    def setUp(self):
        self.book_title = "Atomic habbits"
        self.book_author = "James Klir"
        self.author = Author.objects.create(
            name=self.book_author
        )
        self.book = Book.objects.create(
            title=self.book_title,
            description="Sample Book",
            author=self.author
        )
    
    def test_create_book_successfully(self):
        self.assertEqual(self.book.title, self.book_title)
        self.assertEqual(self.book.description, "Sample Book")
        self.assertEqual(self.book.author, self.author)
    
    def test_book_return(self):
        self.assertEqual(str(self.book), self.book_title)

    def test_book_required_fields_if_blank(self):
        with self.assertRaises(IntegrityError):
            Book.objects.create(title=None, author=self.author)
        
    def test_book_deacription_if_blank(self):
        # with self.assertRaises(IntegrityError):
        Book.objects.create(title="Test", description=None, author=self.author)

    def test_realationship_between_author(self):
        self.assertEqual(self.book.author, self.author)
    
    def test_book_title_unique(self):
        with self.assertRaises(IntegrityError):
            Book.objects.create(title=self.book_title, author=self.author)

    def test_update_book(self):
        self.book.title = "New title"
        self.book.save()
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "New title")

    def test_delete_book(self):
        self.book.delete()
        book = Book.objects.filter(title=self.book_title).exists()
        self.assertFalse(book)
