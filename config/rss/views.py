from django.shortcuts import render, get_object_or_404
from django.views import View 
from .models import Link, Article
from .rss_parser import parse
# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwagrs):

        rsslinks = Link.objects.all()
        context = {"rsslinks":rsslinks}
        return render(request, "rss/index.html", context)
    
index = IndexView.as_view()

def detail(request, pk):
    site = get_object_or_404(Link, pk=pk)
    article_list = parse(site.url)
    for a in article_list:
        article = Article.objects.create(title=a['title'], url=a['url'])
    
    articles = Article.objects.all()
    context = {"articles":articles}
    return render(request, "rss/detail.html", context)

