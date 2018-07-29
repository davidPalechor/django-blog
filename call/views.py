from django.views.generic import ListView

from .models import Call


class CallListView(ListView):
    model = Call
    queryset = Call.objects.all().order_by('-end_date')
    template_name = 'news.html'
