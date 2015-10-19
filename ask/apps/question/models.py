from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    respondent = models.ForeignKey(User, related_name='respondent_id')
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    answer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return '%s' % (self.text)
