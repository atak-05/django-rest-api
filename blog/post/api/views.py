from rest_framework.generics import ListAPIView, RetrieveAPIView,UpdateAPIView, DestroyAPIView
from post.api.serializers import PostSerializers
from post.models import  Post

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    
    
class PostDetailAPIView(RetrieveAPIView):
    queryset  = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'

class PostDeleteAPIView(DestroyAPIView):
    queryset  = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'

class PostUpdateAPIView(UpdateAPIView):
    queryset  = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'