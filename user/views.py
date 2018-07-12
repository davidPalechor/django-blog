from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class UserCreate(CreateView):
    fields = [
        'first_name',
        'last_name',
        'username',
        'email',
        'password'
    ]
    model = User
    success_url = reverse_lazy('app:home')
    template_name = 'signup.html'
