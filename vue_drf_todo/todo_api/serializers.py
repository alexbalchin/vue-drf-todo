from todo_api.models import TodoItem
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'text', 'completed', 'added_date')
