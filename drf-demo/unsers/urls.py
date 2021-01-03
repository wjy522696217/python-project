from django.urls import path,re_path
from . import views
urlpatterns = [
    path("unsers/",views.studentView.as_view()),
    path("unsers2/",views.Student2View.as_view()),
]
