from dataclasses import field, fields
from comment.models import Comment
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers


class CommentCreateSerializers(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created']
        
    def validate (self, attrs):
        if (attrs["parent"]):
            if attrs["parent"].post != attrs["post"]:
                raise serializers.ValidationError("somethinh went wrong")
        return attrs
    
# class CommentChildSerializer(ModelSerializer):
    # class Meta:
        # model= Comment
        # fields= "__all__"
                  

class CommentListSerializers(ModelSerializer):
    replies = SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"
        
    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializers(obj.children(), many=True).data

class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "content"
            ]
                         