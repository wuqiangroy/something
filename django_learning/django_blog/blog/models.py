from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=32)

    # shell中User显示<User: username>而不是<User: User objects>
    def __str__(self):
        return self.username


class Author(models.Model):
    """和Article是一对多关系"""
    user = models.CharField(max_length=32)
    email = models.EmailField()
    add = models.CharField(max_length=256)

    def __str__(self):
        return self.user


class Article(models.Model):
    """和tag是多对多关系"""
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author)
    content = models.TextField()
    tag = models.ManyToManyField("Tag")

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_name = models.CharField(max_length=32)

    def __str__(self):
        return self.tag_name
