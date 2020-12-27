from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .serializer import StudentSeriaizer
from students.models import Student
import json

class  studentView(View):
    def post(self,request):
        data = json.loads(request.body)
        print(data)
        # print(request.body)
        serializer = StudentSeriaizer(data=data)
        ret=serializer.is_valid(raise_exception=True)
        print(ret)
        print(serializer.validated_data)
        print("验证失败",serializer.errors)
        serializer.save()
        
        return HttpResponse("ok")

    def put(self,request):
        "修改数据"
        # 先获取要更新的数据模型对象
        data = json.loads(request.body)
        id = data.get("id")
        student = Student.objects.get(pk=id)
        serializer = StudentSeriaizer(instance=student,data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse("更新完成")



