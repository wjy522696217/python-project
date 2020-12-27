from rest_framework import serializers
from .models import Student
class Studentserializer(serializers.Serializer):
    # 序列化器它本身就是一个类，声明完不会自动调用，我们需要在视图中进行调用
    """学生信息序列化器"""
    # 1. 字段声明

    # 2. 模型序列化器相关声明
    class Meta:
        model = Student
        fields = "__all__"
    # 3. 验证代码[反序列化]

    # 4. 操作数据代码[反序列化器]