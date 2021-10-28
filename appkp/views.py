from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *

class Personview(View):
    form_class=PersonForm
    template='Persons.html'

    def get(self,request,*args,**kwargs):
        form=self.form_class()
        return render(request,self.template,{'form':form})

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            return HttpResponse('successfull'+name)
        return render(request,self.template,{'form':form})



