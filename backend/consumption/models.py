from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Consumption(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    cpu_usage = models.FloatField()
    memory_usage = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.area.name} - {self.timestamp}"
