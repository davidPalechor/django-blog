from django.urls import path

from . import views


app_name = 'call'
urlpatterns = [
    path('news/', views.CallListView.as_view(), name='news'),
    path('create_call/', views.CallCreateView.as_view(), name='create_call'),
]
