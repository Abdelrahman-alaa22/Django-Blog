from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Postapp.urls')),
    path('register/', user_views.SignupView, name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', user_views.Profile, name='profile'),

]





