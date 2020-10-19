from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        fname= request.POST['fname']
        femail= request.POST['femail']
        faddress= request.POST['faddress']
        fmessage= request.POST['fmessage']
        cont = contact(name=fname,email=femail,address=faddress,message=fmessage)
        cont.save()
    return render(request,'index.html')

    

def template(request):
    return render(request,'template.html')

def illustration(request):
    return render(request,'illustration.html')

