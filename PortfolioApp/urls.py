from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('commission/', views.commission),
    path('email/', views.email_request),
    path('aboutus/', views.aboutus),
]