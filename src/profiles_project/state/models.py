from django.db import models

# Create your models here.


class Task(models.Model):

    STATES = (
        ('n', 'new'),
        ('p', 'in_progress'),
        ('d', 'done'),
    )

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True)
    state = models.CharField(choices=STATES, max_length=1, default='n')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="children", blank=True, null=True)