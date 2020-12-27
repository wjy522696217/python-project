from rest_framework.viewsets import ModelViewSet
from .serializers import Student
from .serializers import Studentserializer
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
