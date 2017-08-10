# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models

class Message(models.Model):
        user = models.CharField(max_length=50)
        subject = models.CharField(max_length=200)
        publication_date = models.DateTimeField()
        
        def __unicode__(self):
                return self.subject
          
          
# 日誌
class Diary(models.Model):
        memo = models.TextField()
        time = models.DateTimeField(auto_now_add=True)

# 月份
class Month(models.Model):
        date = models.IntegerField(default=0)