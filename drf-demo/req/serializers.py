from rest_framework import serializers
from students.models import Student

# 字段验证方法
def check_class_num(data):
    if data == "404":
        raise serializers.ValidationError("对不起，没有这个班级")
    return data


class StudentSeriaizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=5)
    sex = serializers.BooleanField(default=1)
    age = serializers.IntegerField(max_value=120, required=True)
    class_num = serializers.CharField(required=True,validators=[check_class_num])
    description = serializers.CharField(allow_null=True, allow_blank=True)

    def validate_name(self,attr):
        if attr == "jack":
            raise serializers.ValidationError("你的姓名不对")
        return attr

    def validate(self,attr):
        if attr.get("age") > 60 and attr.get("sex") ==1:
            raise serializers.ValidationError("对不起，你的年龄不符合要求")

        return attr

    def create(self,validated_data): # 这个参数是由对象给我传进来，validated_data这个验证后成功的数据
        ret = Student.objects.create(**validated_data)
        return ret

    def update(self,instance,validated_data):
        instance.name = validated_data.get("name")
        instance.age = validated_data.get("age")
        instance.sex = validated_data.get("sex")
        instance.class_num = validated_data.get("class_num")
        instance.description = validated_data.get("description")
        instance.save()
        return instance

        # for key, value in validated_data.items():
        #     setattr(instance,key,value)




class Student2Serializer(serializers.ModelSerializer):
    #字段声明
    token = serializers.CharField(read_only=True,default="abc")
    #模型声明，根据模型帮我们生成序列化字段，modelSerializer和我们的模型会自动把字段复制过来给我们用的
    class Meta:
        model = Student # 通过model调用，继承student，然后把它的字段拿过来
        fields = ["id","name","token","age","class_num","description"]
        # fields ="__all__"


        extra_kwargs = {
            "token":{"read_only":True},
            "age":{"min_value":1,"max_value":500},
        }
    #验证方法

    #数据库操作方法

class Student3Serializer(serializers.ModelSerializer):
    #字段声明
    # token = serializers.CharField(read_only=True,default="abc")
    #模型声明，根据模型帮我们生成序列化字段，modelSerializer和我们的模型会自动把字段复制过来给我们用的
    class Meta:
        model = Student # 通过model调用，继承student，然后把它的字段拿过来
        fields = ["id","name"]
        # fields ="__all__"
