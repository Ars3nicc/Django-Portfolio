from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('commission/', views.commission),
    path('programming/', views.programming_projects),
    path('art/', views.art_projects),
    path('email/', views.email_request),
    path('aboutus/', views.aboutus),
]