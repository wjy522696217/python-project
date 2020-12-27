from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    # pass
    #需要进行转换的字段
    name = serializers.CharField()
    age = serializers.IntegerField()
    sex = serializers.BooleanField()
    description = serializers.CharField()