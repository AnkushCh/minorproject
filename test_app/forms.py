from django import forms
from django.contrib.auth.models import User
import csv
from .models import test
class Dataform(forms.Form):
    data_file = forms.FileField()


    def process_data(self):
        print('working')
        f = io.TextIOWrapper(self.cleaned_data['data_file'].file)
        reader = csv.DictReader(f)

        for user in reader:
            print(user)
            User.objects.create_user(username=user['username'],email=user['email'])



# class Testform(forms.Form):
#     subject

class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))