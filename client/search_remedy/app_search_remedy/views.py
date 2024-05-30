from django.shortcuts import render

# Create your views here.
# criar função
def home(request):
    return render(request,'search/home.html')
