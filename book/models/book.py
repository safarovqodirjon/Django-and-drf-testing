from django.db import models


class Book(models.Model):
    title = models.CharField("book title", max_length=100, unique=True)
    description = models.TextField('book description', blank=True, null=True)
    author = models.ForeignKey("book.Author", on_delete=models.CASCADE)

    def __str__(self):
        return self.title