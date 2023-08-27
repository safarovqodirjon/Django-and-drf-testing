from django.db import models

class Author(models.Model):
    name = models.CharField(verbose_name="Author name",
                            max_length=100)

    def __str__(self) -> str:
        return self.name
