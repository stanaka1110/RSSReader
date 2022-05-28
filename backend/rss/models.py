from django.db import models
from .rss_parser import parse
# Create your models here.
class Link(models.Model):

    class Meta:
        db_table = "link"
    
    site_name = models.CharField(verbose_name="site_name", max_length=100)
    url = models.URLField(verbose_name="url")
    article_list = {}

    def article_update(self):
        self.article_list = parse(self.url)
        

    def __str__(self):
        return self.site_name

