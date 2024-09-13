# urls.py
from django.urls import path
from .views import RegisterView
from .views import login_view, logout_view, edit_profile, create_profile, profile_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),  # Страница профиля
    path('profile/edit/', edit_profile, name='edit_profile'),  # URL для редактирования профиля
    path('profile/create/', create_profile, name='create_profile'),
]

   


