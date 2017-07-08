from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=32)

    # shell中User显示<User: username>而不是<User: User objects>
    def __str__(self):
        return self.username
