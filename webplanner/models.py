from __future__ import unicode_literals

from django.db import models

PRIORITY_CHOICES = (
  (1, 'Low'),
  (2, 'Normal'),
  (3, 'High'),
  (4, 'Top')
)

# Create your models here.
class todo(models.Model):  # Table name, has to wrap models.Model to get the functionality of Django.

    title = models.CharField(max_length=200)
    created_date = models.DateField(auto_now=True)
    start_date = models.DateField(blank=True, null=True, )
    due_date = models.DateField(blank=True, null=True, )
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(blank=True, null=True)
    estimated_date = models.DateField(blank=True, null=True)
    time_estimated = models.IntegerField(blank=True, null=True, default=12)
    time_spent = models.IntegerField(blank=True,null=True)
    priority = models.PositiveIntegerField(choices=PRIORITY_CHOICES, default=1)

    class Meta:
        ordering = ['-priority', '-due_date', 'created_date']

    def __unicode__(self):
        # Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.title