from django.db import models

# Create your models here.
class LibraryBook(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва")
    author = models.CharField(max_length=100, verbose_name="Автор")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    available = models.BooleanField(default=True, verbose_name="Доступна")

    class Meta:
        ordering = ['author']
        indexes = [
            models.Index(fields=['isbn'], name='isbn_idx')
        ]

    def __str__(self):
        return f"{self.title} ({self.author})"
