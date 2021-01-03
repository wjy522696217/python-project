from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from students.models import Student
from .serializers import Student2Serializer,Student3Serializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin


class StudentAPI1View(APIView):
    def get(self, request):
        print(request)
        print(request._request)
        print(request.query_params)
        print(request.query_params.get("user"))
        print(request.query_params.getlist("love"))
        response = Response("ok", status=status.HTTP_300_MULTIPLE_CHOICES)
        response.set_cookie("username", "wjy")
        response["company"] = "huberbuy"
        return response

    def post(self, request):
        print(request.data)
        return Response("ok")


class StudentAPI2View(APIView):
    def get(self, request):
        student_list = Student.objects.all()
        serializer = Student2Serializer(instance=student_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Student2Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentAPI3View(APIView):
    def get(self, request, pk):
        student_obj = Student.objetcs.get(pk=pk)
        serializer = Student2Serializer(instance=student_obj)
        return Response(serializer.data)

    def put(self, request, pk):
        student_obj = Student.objetcs.get(pk=pk)
        serializer = Student2Serializer(instance=student_obj)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        Student.objetcs.delete(pk=pk)
        return Response({"message": "delete ok"}, status=status.HTTP_200_OK)

class StudentAPI4View(GenericAPIView):
    # serializer_class = Student2Serializer
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return Student3Serializer
        else:
            return Student2Serializer

    def get(self, request):
        serializer = self.get_serializer(instance=self.get_queryset(),many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

'''
视图扩展类，一般都会配合GenericsAPIView或者视图扩展类
'''
class StudentAPI5View(GenericAPIView,ListModelMixin,CreateModelMixin):
    serializer_class = Student2Serializer
    queryset = Student.objects.all()
    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)


class StudentAPI6View(GenericAPIView, RetrieveModelMixin,UpdateModelMixin):
    serializer_class = Student2Serializer
    queryset = Student.objects.all()

    def get(self, request,pk):
        return self.retrieve(request,pk)

    def put(self, request,pk):
        return self.update(request,pk)

