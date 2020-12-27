from django.shortcuts import render
from django.views import View
from .serializers import StudentSerializer
from django.http import HttpResponse,JsonResponse
from students.serializers import Student

class StudentView(View):
    def get1(self,request):
        # 实例化序列化器，创建序列化器对象
        # Serializer = StudentSerializer()
        # print(Serializer.data)
        student_list = Student.objects.all()
        print(student_list)
        Serializer = StudentSerializer(instance=student_list,many=True)
        print(Serializer.data)
        # return HttpResponse("ok")
        return JsonResponse(Serializer.data,safe=False)

    def get(self,request):
        student1 = Student.objects.all().first()
        print(student1)

        Serializer = StudentSerializer(instance=student1)
        print(Serializer.data)
        # return HttpResponse("ok")
        return JsonResponse(Serializer.data)




