from rest_framework import serializers
from students.models import Student

# 字段验证方法
def check_class_num(data):
    if data == "404":
        raise serializers.ValidationError("对不起，没有这个班级")
    return data


class StudentSeriaizer(serializers.Serializer):
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
