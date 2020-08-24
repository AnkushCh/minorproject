from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',home,name='home'),
    path('test',test,name='test'),
    path('create-test',create_test,name='create-test'),
    path('upload',upload,name='upload'),
    path('download',download,name='download'),
    path('ajax/next_ques',next_ques,name='next-ques'),
    path('ajax/get_ans',get_ans,name='get-ans'),
    path('ajax/quiz_data',quiz_data,name='quiz-data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)