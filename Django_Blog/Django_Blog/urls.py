from django.contrib import admin
from django.urls import path, include
from user import views as user_views
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Postapp.urls')),
    path('register/', user_views.SignupView, name='register'),

]





