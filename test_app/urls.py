from django.urls import path
from django.conf.urls import url
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',home,name='home'),
    path('test',test,name='test'),
    url(r'^accounts/profile/$',get_user_profile,name='user_profile'),
    path('dashboard',dashboard,name='dashboard'),
    path('create-test',create_test,name='create-test'),
    path('upload',upload,name='upload'),
    path('download',download,name='download'),
    path('ajax/next_ques',next_ques,name='next-ques'),
    path('ajax/get_ans',get_ans,name='get-ans'),
    path('ajax/quiz_data',quiz_data,name='quiz-data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)