from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from favourite.api.serializers import FavouriteAPISerializer
from favourite.api.paginations import FavouritePagination
from favourite.models import Favourite
from favourite.api.serializers import FavouriteListCreateAPISerializer

class FavouriteListCreateAPIView(ListCreateAPIView):
    # queryset = Favourite.objects.all()
    serializer_class = FavouriteListCreateAPISerializer
    pagination_class = FavouritePagination

    def get_queryset(self):
        return Favourite.objects.filter(user = self.request.user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class FavouriteAPIView(RetrieveUpdateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerializer
    lookup_field= 'pk'
    
