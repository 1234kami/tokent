from django.db import models
from django.db import models


class Task(models.Model):
    CHOICE_TYPE = (
        ('work', 'Work'),
        ('home', 'Home'),
        ('edu', 'Edu')
    )
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    type = models.CharField(max_length=25, choices=CHOICE_TYPE)

    def __str__(self):
        return self.title
# Create your models here.
