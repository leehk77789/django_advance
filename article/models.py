from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model


class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="작성자")
    title = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return str(self.title)