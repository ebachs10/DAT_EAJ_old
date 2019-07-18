from django.views.generic import ListView

from .models import Journal

class JournalListView(ListView):
    model = Journal
    template_name = 'journal_list.html'