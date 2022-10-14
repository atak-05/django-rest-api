
from django.urls import path,include
from .views import FavouriteListCreateAPIView


app_name="favourite"
urlpatterns = [
    path('list-create/', FavouriteListCreateAPIView.as_view(), name='list-create'),
]

