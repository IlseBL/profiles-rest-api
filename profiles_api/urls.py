from django.urls import path

from profiles_api import views


urlspatterns = [
    path('hello-view', views.HelloAPIView.as_view())
]
