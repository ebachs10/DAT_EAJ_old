
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Journal

class JournalListView(ListView):
    model = Journal
    template_name = 'journal_list.html'
    login_url = 'login'

class JournalCreateView(LoginRequiredMixin, CreateView):
    model = Journal
    template_name = 'journal_new.html'
    fields = ('AnimalType' , 'TagNumber' , 'disease' , 'note')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class JournalDetailView(LoginRequiredMixin, DetailView):
    model = Journal
    template_name = 'journal_detail.html'  
    login_url = 'login'

class JournalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Journal
    fields = ('TreatmentStatus', 'note',)
    template_name = 'journal_edit.html'  
    login_url = 'login'  

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user         

class JournalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Journal
    template_name = 'journal_delete.html'
    success_url = reverse_lazy('journal_list')
    login_url = 'login'    

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
