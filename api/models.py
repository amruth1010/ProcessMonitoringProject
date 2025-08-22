from django.db import models

# Create your models here.

class Process(models.Model):
    hostname = models.CharField(max_length=100)
    pid = models.IntegerField()
    parent_pid = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200)
    cpu = models.FloatField()
    memory = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.pid})"