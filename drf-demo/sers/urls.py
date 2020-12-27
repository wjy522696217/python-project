from django.urls import path,re_path
from . import views
urlpatterns=[
    path('sers/', views.StudentView.as_view()),
]