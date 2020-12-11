from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'bokete'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
]    
    