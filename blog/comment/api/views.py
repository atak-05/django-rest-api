from rest_framework.generics import CreateAPIView

from comment.api.serialiizers import CommentCreateSerializers
from comment.models import Comment

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializers