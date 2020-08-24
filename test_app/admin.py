from django.contrib import admin
from .models import *
# Register your models here.

class quizAdmin(admin.ModelAdmin):
    list_display= ('subject','qn', 'op1','op2','op3','op4', 'ans', 'level')
    
class TestAdmin(admin.ModelAdmin):
    list_display=('name','quiz')

admin.site.register(quiz,quizAdmin)
admin.site.register(test,TestAdmin)
admin.site.register(Profile)