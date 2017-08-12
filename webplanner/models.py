from __future__ import unicode_literals

from django.db import models

# Create your models here.
class todo(models.Model):  # Table name, has to wrap models.Model to get the functionality of Django.

    taskID = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()  # Like a TEXT field
    created = models.DateTimeField()  # Like a DATETIME fieldma

    def __unicode__(
            self):  # Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name