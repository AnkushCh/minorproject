from django.shortcuts import render
import django_excel as excel
from .forms import Dataform,UploadFileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
import csv
from django.db.models import Max,Min
from .models import quiz
import json
import random
from django.core.serializers import serialize

# Create your views here.


def home(request):
    return render(request,'base.html')

def test(request):
    sub = sorted(set(i.subject for i in quiz.objects.all()))
    return render(request,'test.html',{'sub':sub})

def rand(sub):
    min_id = quiz.objects.filter(subject=sub).aggregate(min_id=Min('id'))['min_id']
    max_id = quiz.objects.filter(subject=sub).aggregate(max_id=Max('id'))['max_id']
    while True:
        pk = random.randint(min_id,max_id)
            
        js_data = quiz.objects.get(pk=pk)
        if js_data:
            data ={
                    'pk':js_data.pk,
                    'qn':js_data.qn,
                    'op1':js_data.op1,
                    'op2':js_data.op2,
                    'op3':js_data.op3,
                    'op4':js_data.op4,
            }
            # print('sent')
            break  
    return data  


def next_ques(request):
    if request.is_ajax:
        subj = request.GET.get('subject')
        # data=rand(subj)
        return JsonResponse({'data':json.dumps(rand(subj))})

def get_ans(request):
    if request.is_ajax:
        ans = request.GET.get('option')
        pk = request.GET.get('qid')
        obj=quiz.objects.get(pk=pk)
        data = {
            'ans':obj.ans
        }
        return JsonResponse({'data':json.dumps(data)})


def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
        files = request.FILES.getlist('myfile')
        for f in files:

            f.save_to_database(
            model=quiz,
            # initializer=[None],
            mapdict=['subject','qn','op1','op2','op3','op4','ans','level'],
        )
        return redirect('home')
        # return render(request, 'upload_file.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })
    else:
        form = UploadFileForm()
        # print('not ok')
    return render(request, 'upload_file.html',{'form':form})

def download(request):
    sheet = excel.pe.Sheet([[1, 2],[3, 4]])
    return excel.make_response(sheet, "csv")