from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.db import IntegrityError

from .forms import CallCreationForm
from .models import Call


class CallListView(ListView):
    queryset = Call.objects.all().order_by('-end_date')
    template_name = 'news.html'


class CallCreateView(LoginRequiredMixin, CreateView):
    form_class = CallCreationForm
    login_url = reverse_lazy('user:login')
    model = Call
    redirect_field_name = 'next'
    success_url = reverse_lazy('home')
    template_name = 'create_call.html'

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error(
                None,
                'Call for this period already exists.'
            )
            return self.form_invalid(form)
