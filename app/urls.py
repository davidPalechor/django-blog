from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from . import views


app_name = 'app'
urlpatterns = [
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('images/favicon.ico'))
    ),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('account/', include('user.urls', namespace='user')),
    path('calls/', include('call.urls', namespace='call')),
]
