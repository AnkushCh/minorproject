from django.db import models
from django.contrib.auth.models import Group
# Create your models here.
class quiz(models.Model):
    subject = models.CharField(max_length=500)
    qn = models.CharField(max_length=500)
    op1 = models.CharField(max_length=500)
    op2 = models.CharField(max_length=500)
    op3 = models.CharField(max_length=500)
    op4 = models.CharField(max_length=500)
    ans = models.IntegerField()
    level = models.IntegerField(default=1)
