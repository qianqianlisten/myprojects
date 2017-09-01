from django.db import models

import datetime
from django.utils import timezone
# Create your models here

class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=30)
    pub_date = models.DateTimeField()

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __unicode__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text