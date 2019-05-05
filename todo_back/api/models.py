from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length=150)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Task(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField('date created')
    due_on = models.DateTimeField('date due')
    status = models.CharField(max_length=150)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_part_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status
        }

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created': self.created_at,
            'due': self.due_on,
            'status': self.status,
            'task_list_name': self.task_list.name
        }
