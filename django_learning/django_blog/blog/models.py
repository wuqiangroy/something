from django.db import models
import ast


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


# 自定义Field
class ListField(models.TextField):

    description = "store a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection, context):
        return value

    def to_python(self, value):
        if not value:
            value = []
        if isinstance(list, value):
            return value
        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return str(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class Country(models.Model):
    name = ListField()
