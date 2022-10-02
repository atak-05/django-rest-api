from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateAPIView,
                                     DestroyAPIView,
                                     CreateAPIView,)
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

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset  = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'
    
class PostCreateAPIView(CreateAPIView):
    queryset  = Post.objects.all()
    serializer_class = PostSerializers
    #Burada sorguyu yazan user görüntülemek için bu mettotu kullandık#
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)
        
        #mail gönderme işlemleride burada yapabiliriz
        