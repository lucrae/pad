from django.db import models

class Entry(models.Model):
    body = models.TextField(max_length=1024)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return "Entry({}, {})".format(self.body, self.archived)