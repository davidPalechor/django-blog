from django.contrib.auth.models import User
from django.views.generic.edit import CreateView


class UserCreate(CreateView):
    fields = [
        'first_name',
        'last_name',
        'username',
        'email',
        'password'
    ]
    model = User
    success_url = '/'
    template_name = 'signup.html'
