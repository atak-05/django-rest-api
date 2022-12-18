from cgitb import lookup
from dataclasses import field, fields
from rest_framework import serializers
from post.models import Post
# class PostSerializers(serializers.Serializer):
    # title = serializers.CharField(max_length=120)
    # content = serializers.CharField(max_length=200)
    
class PostSerializers(serializers.ModelSerializer):
    url = serializers.  HyperlinkedIdentityField(
    view_name='post:detail',
    lookup_field = 'slug'
 )
    username = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = [ 
                 'username',
                 'title',
                 'content',
                 'image',
                 'url',
                 'created',
                 'modified_by',
                 'draft'
                  ]
    def get_username(self, obj):
        return str(obj.user.username)
        
class PostUpdateCreateSerializer(serializers.ModelSerializer):
   
   
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]






        


                            








        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        