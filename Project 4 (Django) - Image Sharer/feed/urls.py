from django.urls import path

from .views import HomePageView, PostDetailView, AddPostView, HomePage

app_name='feed'

urlpatterns =[
    path('',HomePage.as_view(),name='index'),
    path('detail/<int:pk>/',PostDetailView.as_view(), name='detail'),
    path('post/',AddPostView.as_view(),name='post'),
]