from django.urls import path
from . import views
from .views import LinkListCreateAPIView, LinkRetrieveUpdateDestroyAPIView

app_name = "rss"


urlpatterns = [ 
    path('links/', LinkListCreateAPIView.as_view()),
    path('links/<pk>', LinkRetrieveUpdateDestroyAPIView.as_view()),
    ]
