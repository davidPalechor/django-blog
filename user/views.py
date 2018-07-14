from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import SignupForm


class UserCreate(CreateView):
    form_class = SignupForm
    model = User
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
