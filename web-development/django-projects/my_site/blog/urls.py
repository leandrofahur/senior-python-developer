from django.urls import path

urlpatterns = [
    path('/'),
    path('/posts'),
    path('/posts/<slug:slug>'),
]
