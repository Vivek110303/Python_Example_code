from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from Helloworld.models import post
from Helloworld.serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated
from Helloworld.permissions import IsPostPossessor
from rest_framework import filters
from Helloworld.filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend
class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response({'message': 'helloworld'})


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    queryset = post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend ,filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PostFilter
    ordering_fields = ['id']
    search_fields = ('title', 'content')

    def get_queryset(self):
         return post.objects.filter(created_by=self.request.user)
