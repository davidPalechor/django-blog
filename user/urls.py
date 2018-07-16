from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'user'
urlpatterns = [
    path('signup/', views.UserCreate.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
