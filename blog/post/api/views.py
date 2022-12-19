from venv import create
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateAPIView,
                                     DestroyAPIView,
                                     CreateAPIView,)
from post.api.paginations import PostPagination
#Custom permission
from post.api.permissions import IsOwner
from post.api.serializers import PostSerializers
from post.models import  Post
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import(
    IsAuthenticated,
)
#Create Model Mixin
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,)

class PostListAPIView(ListAPIView): #Create Model Mixini de ekleyerek aynı sayfada hem ekleme hemde listeleme yapabiliriz.
    serializer_class = PostSerializers
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    pagination_class= PostPagination
    
    def get_queryset(self):#filtreleme özelliği
        queryset = Post.objects.filter(draft=False)
        return queryset
    
    # def post(self, request,*args, **kwargs):
        # return self.create(request,*args, **kwargs)
    # #Postu oluşturan kullanıcın kendisi olmasını için bunu yapıyoruz.
    # def perform_create(self, serializer):
        # serializer.save(user = self.request.user)   
    
class PostDetailAPIView(RetrieveAPIView):
    queryset  = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'

# class PostDeleteAPIView(DestroyAPIView):
    # queryset  = Post.objects.all()
    # serializer_class = PostSerializers
    # lookup_field = 'slug'
    # permission_classes = [IsOwner]  

class PostUpdateAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset  = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'
    permission_classes = [IsOwner]
    def perform_update(self, serializer):
        serializer.save(modified_by = self.request.user)   
        
    def delete(self, request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
class PostCreateAPIView(CreateAPIView):
    queryset  = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticated]
    #Burada sorguyu yazan user görüntülemek için bu mettotu kullandık#
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)
        
        #mail gönderme işlemleride burada yapabiliriz
     
   
        
        