from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Link
from rest_framework import views, status
from .serializer import LinkSerializer
# Create your views here.


class LinkListCreateAPIView(views.APIView):
    
    def get(self, request, *args, **kwargs):
        link_list = Link.objects.all()
        serializer = LinkSerializer(instance=link_list, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class LinkRetrieveUpdateDestroyAPIView(views.APIView):

    def get(self, request, pk, *args, **kwargs):

        link = get_object_or_404(Link, pk=pk)
        link.article_update()
        serializer = LinkSerializer(instance=link)

        return Response(serializer.data, status.HTTP_200_OK)

