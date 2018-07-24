from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView

from .forms import SignupForm


class UserCreate(CreateView):
    form_class = SignupForm
    model = User
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form['user'].save()
        student_info = form['student_info'].save(commit=False)
        student_info.user = user
        student_info.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)
