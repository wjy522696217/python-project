from django.urls import path,re_path
from . import views
urlpatterns = [
    path("view1/",views.StudentAPI1View.as_view()),
    path("view2/",views.StudentAPI2View.as_view()),
    path("view3/",views.StudentAPI3View.as_view()),
    path("view4/",views.StudentAPI4View.as_view()),
    re_path("^view/(?P<pk>\d+)/$",views.StudentAPI5View.as_view())
]
