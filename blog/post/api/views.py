from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateAPIView,
                                     DestroyAPIView,
                                     CreateAPIView,)
#Custom permission
from post.api.permissions import IsOwner
from post.api.serializers import PostSerializers
from post.models import  Post
from rest_framework.filters import SearchFilter
from rest_framework.permissions import(
    IsAuthenticated,
    IsAdminUser,
)

class PostListAPIView(ListAPIView):
    serializer_class = PostSerializers
    filter_backends = [SearchFilter]
    search_fields = ['title']
    
    def get_queryset(self):#filtreleme özelliği
        queryset = Post.objects.filter(draft=False)
        return queryset
    
    
class PostDetailAPIView(RetrieveAPIView):
    queryset  = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'

class PostDeleteAPIView(DestroyAPIView):
    queryset  = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'
    permission_classes = [IsOwner]  

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset  = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'
    permission_classes = [IsOwner]
    def perform_update(self, serializer):
        serializer.save(modified_by = self.request.user)   
class PostCreateAPIView(CreateAPIView):
    queryset  = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticated]
    #Burada sorguyu yazan user görüntülemek için bu mettotu kullandık#
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)
        
        #mail gönderme işlemleride burada yapabiliriz
     
   
        
        