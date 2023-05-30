from django.shortcuts import render

# Create your views here.

def oneplus(request):
    d={'name':'Ajit','surname':'Kumar'}
    return render(request,'wish.html',context=d)