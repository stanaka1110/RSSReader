from django.db import models

# Create your models here.
class Link(models.Model):

    class Meta:
        db_table = "link"
    
    site_name = models.CharField(verbose_name="site_name", max_length=100)
    url = models.URLField(verbose_name="url")

    def __str(self):
        return self.site_name

class Article(models.Model):
    class Meta:
        db_table = "article"

    title = models.CharField(verbose_name="title", max_length=200)
    url = models.URLField(verbose_name="url")

    def __str__(self):
        return self.title