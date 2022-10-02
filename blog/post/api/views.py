from rest_framework.generics import ListAPIView
from post.api.serializers import PostSerializers
from post.models import  Post

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers