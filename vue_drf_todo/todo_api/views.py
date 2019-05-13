from django.shortcuts import render
from rest_framework import viewsets
from todo_api.models import TodoItem
from todo_api.serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint allows Todo items to be viewed or edited.
    """
    queryset = TodoItem.objects.all().order_by('-added_date')
    serializer_class = TodoSerializer
