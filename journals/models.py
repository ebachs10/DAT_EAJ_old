from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

ANIMAL_TYPES = (
    ('sow','SOW'),
    ('cow', 'COW'),
    ('sheep','SHEEP'),
)

DISEASE_TYPES = (
    ('diarrhea','DIARRHEA'),
    ('bedsore', 'BEDSORE'),
)



class Journal(models.Model):
    AnimalType = models.CharField(max_length=3, choices = ANIMAL_TYPES , default = 'sow')
    TagNumber = models.CharField(max_length=255)
    disease = models.CharField(max_length=2, choices = DISEASE_TYPES , default = 'diarrhea')
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)

    def __str__(self):
        return self.TagNumber

    def get_absolute_url(self):
        return reverse('journal_detail', args=[str(self.id)])        
