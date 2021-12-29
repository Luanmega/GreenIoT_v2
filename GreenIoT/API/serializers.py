from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Metal:
        model = Todo
        fields = ('id', 'title',)