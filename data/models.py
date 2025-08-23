from django.db import models

# Create your models here.
class Author (models.Model):
    id=models.AutoField(primary_key=True)
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
        constraints=[
            models.UniqueConstraint(fields=['name','lastname'], name='unique_name_email')
        ]
class Category (models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    class Meta:
        db_table = 'Category'
        ordering = ['name']
        verbose_name_plural = 'categories'
        verbose_name = 'category'
class Post (models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Post'
        ordering = ['created']
        verbose_name_plural = 'posts'
        verbose_name = 'post'