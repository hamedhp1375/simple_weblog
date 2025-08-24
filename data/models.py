from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Author'
        ordering = ['created']
        verbose_name_plural = 'authors'
        verbose_name = 'author'
        constraints = [
            models.UniqueConstraint(fields=['name', 'lastname'], name='unique_name_lastname')
        ]


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'Category'
        ordering = ['name']
        verbose_name_plural = 'categories'
        verbose_name = 'category'


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'Tag'
        ordering = ['name']
        verbose_name_plural = 'tags'
        verbose_name = 'tag'


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag,blank=True)

    class Meta:
        db_table = 'Post'
        ordering = ['created']
        verbose_name_plural = 'posts'
        verbose_name = 'post'


class User(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    id_code = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(9999999999)
        ]

        , unique=True)

    class Meta:
        db_table = 'user'
        ordering = ['id_code']
        verbose_name_plural = 'users'
        verbose_name = 'user'


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Comment'
        ordering = ['created']
        verbose_name_plural = 'comments'
        verbose_name = 'comment'
