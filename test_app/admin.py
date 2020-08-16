from django.contrib import admin
from .models import quiz
# Register your models here.

class quizAdmin(admin.ModelAdmin):
    list_display= ('subject','qn', 'op1','op2','op3','op4', 'ans', 'level')
    

admin.site.register(quiz,quizAdmin)