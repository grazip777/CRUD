from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    birthday = models.DateField()

    def __str__(self):
        return self.username
