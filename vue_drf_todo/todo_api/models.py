from django.db import models

class TodoItem(models.Model):
    text = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
