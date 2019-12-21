from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=30, null=False)
    post = models.TextField(max_length=4000, null=False)

    def __str__(self):
        return self.name

