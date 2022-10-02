from dataclasses import field, fields
from rest_framework import serializers
from post.models import Post
# class PostSerializers(serializers.Serializer):
    # title = serializers.CharField(max_length=120)
    # content = serializers.CharField(max_length=200)
    
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [ 
                 'user',
                 'title',
                 'content',
                 'image',
                 'slug',
                 'created',
                  ]







        


                            








        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        