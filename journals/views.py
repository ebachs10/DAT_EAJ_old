from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Journal

class JournalListView(ListView):
    model = Journal
    template_name = 'journal_list.html'

class JournalCreateView(CreateView):
    model = Journal
    template_name = 'journal_new.html'
    fields = ('AnimalType' , 'TagNumber' , 'disease' , 'note' , 'author')

class JournalDetailView(DetailView):
    model = Journal
    template_name = 'journal_detail.html'  

class JournalUpdateView(UpdateView):
    model = Journal
    fields = ('TreatmentStatus', 'note',)
    template_name = 'journal_edit.html'     

class JournalDeleteView(DeleteView):
    model = Journal
    template_name = 'journal_delete.html'
    success_url = reverse_lazy('journal_list')
