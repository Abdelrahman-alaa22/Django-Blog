from django.urls import path
from .views import Home, DetailPost, PostCreate, UpdatePost, DeletePost
from . import views


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<int:pk>', DetailPost.as_view(), name='post-details'),
    path('create/', PostCreate.as_view(), name='createpost'),
    path('post/<int:pk>/update/', UpdatePost.as_view(), name='updateview'),
    path('post/<int:pk>/delete/', DeletePost.as_view(), name='updateview'),

]




