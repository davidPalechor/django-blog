from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'user'
urlpatterns = [
    path('signup/', views.UserCreate.as_view(), name='signup'),
]
