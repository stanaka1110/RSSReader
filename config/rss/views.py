from django.shortcuts import render
from django.views import View 
from .models import Link
from django.http import HttpResponse
# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwagrs):

        rsslinks = Link.objects.all()
        context = {"rsslinks":rsslinks}
        return render(request, "rss/index.html", context)
    
index = IndexView.as_view()

def detail(request, pk):
    context = {test:"test"}
    return render(request, "rss/index.html", context)
