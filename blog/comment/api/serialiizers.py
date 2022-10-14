from dataclasses import field, fields
from comment.models import Comment
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from django.contrib.auth.models import User
from post.models import Post


class CommentCreateSerializers(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created']

    def validate(self, attrs):
        if (attrs["parent"]):
            if attrs["parent"].post != attrs["post"]:
                raise serializers.ValidationError("somethinh went wrong")
        return attrs

# class CommentChildSerializer(ModelSerializer):
    # class Meta:
        # model= Comment
        # fields= "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'id', 'email')


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'id')


class CommentListSerializers(ModelSerializer):
    replies = SerializerMethodField()
    user = UserSerializer()
    post = PostCommentSerializer()

    class Meta:
        model = Comment
        fields = "__all__"
        # depth = 1

    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializers(obj.children(), many=True).data


class CommentDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "content"
        ]
