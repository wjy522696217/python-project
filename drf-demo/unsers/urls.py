from django.urls import path,re_path
from . import views
urlpatterns = [
    path("unsers/",views.studentView.as_view()),
]
