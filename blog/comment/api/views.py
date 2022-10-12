from rest_framework.generics import CreateAPIView, ListAPIView

from comment.api.serialiizers import CommentCreateSerializers, CommentListSerializers 
from comment.models import Comment

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializers
    
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)
        
class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializers
    
    def get_queryset(self):
        return Comment.objects.filter(parent= None)