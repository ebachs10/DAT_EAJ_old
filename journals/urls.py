# journals/urls.py
from django.urls import path
from .views import(
    JournalListView,
    JournalUpdateView,
    JournalDetailView,
    JournalDeleteView,
    JournalCreateView,
)
urlpatterns = [
    path('<int:pk>/edit/', JournalUpdateView.as_view(), name = 'journal_edit'),
    path('<int:pk>/', JournalDetailView.as_view(), name = 'journal_detail'),
    path('<int:pk>/delete/', JournalDeleteView.as_view(), name = 'journal_delete'),    
    path('new/' , JournalCreateView.as_view(), name = 'journal_new'),
    path('', JournalListView.as_view(), name='journal_list'),
]