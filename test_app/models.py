from django.db import models
from django.contrib.auth.models import Group,User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    


class quiz(models.Model):
    subject = models.CharField(max_length=500)
    qn = models.CharField(max_length=500,unique=True)
    op1 = models.CharField(max_length=500)
    op2 = models.CharField(max_length=500)
    op3 = models.CharField(max_length=500)
    op4 = models.CharField(max_length=500)
    ans = models.IntegerField()
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.subject + ':' + self.qn


class test(models.Model):
    name = models.CharField(max_length=50)
    quiz = models.ForeignKey(quiz,on_delete=models.PROTECT)

    def __str__(self):
        return self.name