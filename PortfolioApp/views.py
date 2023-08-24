from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'components/home.html')
def aboutus(request):
    return render(request, 'components/about.html')