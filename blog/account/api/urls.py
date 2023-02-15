
from rest_framework import serializers
from django.urls import path, include

from account.api.view import (
        ProfileView, 
)

app_name = "account"
urlpatterns = [
    path('me', ProfileView.as_view(), name='me'),
]
