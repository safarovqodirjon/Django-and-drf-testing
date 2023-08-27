from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from ..models import Author
from ..serializers import AuthorSerializer

AUTHOR_URL = reverse("book:author-list")


class BookModelAPITest(TestCase):
    @staticmethod
    def create_author(**kwargs):
        defaults = {
            "name": "Steve Jobs"
        }
        defaults.update(kwargs)

        author = Author.objects.create(**defaults)
        return author

    @staticmethod
    def detail_url(author_id):
        return reverse('book:author-detail', args=[author_id])
    
    def setUp(self):
        self.author_name = "Steve Jobs"
        self.client = APIClient()
    
    def test_create_author_api(self):
        author_data = {
            "name": self.author_name
        }
        result = self.client.post(AUTHOR_URL, author_data)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

        author = Author.objects.get(name=author_data['name'])
        self.assertEqual(author.name, author_data['name'])

    def test_update_author_api(self):
        author = self.create_author()
        author_update_data = {
            "name": "James Klir"
        }
        url = self.detail_url(author.id)
        result = self.client.patch(url, author_update_data)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        author.refresh_from_db()
        self.assertEqual(author.name, 'James Klir')
    
    def test_delete_author_api(self):
        author = self.create_author()

        url = self.detail_url(author.id)
        result = self.client.delete(url)
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)
        author = Author.objects.filter(id=author.id).exists()
        self.assertFalse(author)
    
    def test_list_author_api(self):
        self.create_author()
        result = self.client.get(AUTHOR_URL)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        author = Author.objects.all().order_by('id')
        serializer = AuthorSerializer(author, many=True)
       
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data, serializer.data)
    
    def test_retrieve_author_api(self):
        author = self.create_author()

        url = self.detail_url(author.id)
        result = self.client.get(url)

        serializer = AuthorSerializer(author)

        self.assertEqual(result.data, serializer.data)
