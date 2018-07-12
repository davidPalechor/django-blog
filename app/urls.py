from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView


app_name = 'app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('account/', include('user.urls', namespace='user')),
]
