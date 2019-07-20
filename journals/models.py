from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

ANIMAL_TYPES = (
    ('sow','Sow'),
    ('cow', 'Cow'),
    ('sheep','Sheep'),
)

DISEASE_TYPES = (
    ('diarrhea','DIARRHEA'),
    ('bedsore', 'BEDSORE'),
)

TREATMENT_STATUS = (
    ('ok','Ok'),
    ('warning', 'Warning'),
    ('warning', 'Warning'),
    ('critical', 'Critical'),
)

class Journal(models.Model):
    AnimalType = models.CharField(max_length=255, choices = ANIMAL_TYPES , default = 'sow')
    TagNumber = models.CharField(max_length=255)
    disease = models.CharField(max_length=255, choices = DISEASE_TYPES , default = 'diarrhea')
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    TreatmentStatus = models.CharField(max_length=255, choices = TREATMENT_STATUS , default = 'sow')
    Location = models.CharField(max_length=255 , default = 'Optional to set location')

    def __str__(self):
        return self.AnimalType + ' ' + self.TagNumber

    def get_absolute_url(self):
        return reverse('journal_detail', args=[str(self.id)])        

class Comment(models.Model):
    journal = models.ForeignKey(Journal, 
                                on_delete = models.CASCADE,
                                related_name = 'comments')        
    comment = models.CharField(max_length = 140)
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE,)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('journal_list')
    
