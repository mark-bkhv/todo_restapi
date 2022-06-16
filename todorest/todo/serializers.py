from django.contrib.auth.models import User
from rest_framework import serializers

from todo.models import Todo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class TodoSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Todo
        fields = ['id','name', 'date_created', 'done', 'owner']
