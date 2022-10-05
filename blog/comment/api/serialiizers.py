from comment.models import Comment
from rest_framework.serializers import ModelSerializer

class CommentCreateSerializers(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created']