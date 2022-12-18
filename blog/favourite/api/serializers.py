from rest_framework.serializers import ModelSerializer
from favourite.models import Favourite
from rest_framework import serializers




class FavouriteListCreateAPISerializer(ModelSerializer):
    class Meta:
        model  = Favourite
        fields= '__all__'
        
    def validate(self, attrs):
        queryset = Favourite.objects.filter(post = attrs["post"], user = attrs["user"])
        if queryset.exists():
            raise serializers.ValidationError("Already added to favorites")
        return attrs
    
