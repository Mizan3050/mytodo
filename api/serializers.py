# Serializer allows us to return data as response in json format
from rest_framework import serializers
from .models import Task

# specify which model you want to serialize
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
