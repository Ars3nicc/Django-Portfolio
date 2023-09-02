from django.shortcuts import (
    render, 
    get_object_or_404,
    redirect,
    HttpResponse,
    HttpResponseRedirect
)
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def base(request):
    return render(request, 'base.html')
def home(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            'Contact Form',
            message,
            'settings.EMAIL_HOST_USER',
            ['franzroninm@gmail.com', 'frm.manrique@gmail.com'],
            fail_silently=True
        )
    return render(request, 'components/home.html')
def commission(request):
    return render(request, 'components/404.html')

def programming_projects(request):
    return render(request, 'components/programming.html')

def art_projects(request):
    return render(request, 'components/404.html')


def aboutus(request):
    return render(request, 'components/about.html')

def email_request(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            'Contact Form',
            message,
            'settings.EMAIL_HOST_USER',
            ['franzroninm@gmail.com'],
            fail_silently=True
        )
    return render(request, 'components/email_test.html')