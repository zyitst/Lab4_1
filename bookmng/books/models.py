from django.db import models

class Author(models.Model):
    AuthorID = models.CharField(max_length=5, primary_key=True)
    Name = models.CharField(max_length=50)
    Age = models.CharField(max_length=3)
    Country = models.CharField(max_length=48)
    def __unicode__(self):
        return self.Name
class Publisher(models.Model):
    Name = models.CharField(max_length=30)
    Country = models.CharField(max_length=24)
class Book(models.Model):
    ISBN = models.CharField(max_length=15, primary_key=True)
    Title = models.CharField(max_length=36)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=36)
    PublishDate = models. DateField(null=True, blank=True)
    Price = models.CharField(max_length=6)
    def __unicode__(self):
        return self.Title
    class Meta:
        ordering = ['Title']
#修改model.py
