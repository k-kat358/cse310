
from django.db import models

class Guides(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=200)
    cpu = models.TextField()
    cpu_cooler = models.TextField()
    motherboard = models.TextField()
    memory = models.TextField()
    storage = models.TextField()
    gpu = models.TextField()
    psu = models.TextField()
    case = models.TextField()

    def __str__(self):
        return self.title

class GuidesImages(models.Model):
    guide = models.ForeignKey(Guides, on_delete=models.CASCADE, related_name='images')
    component = models.CharField(max_length=50, choices=[
        ('CPU', 'CPU'),
        ('CPU Cooler', 'CPU Cooler'),
        ('Motherboard', 'Motherboard'),
        ('Memory', 'Memory'),
        ('Storage', 'Storage'),
        ('GPU', 'GPU'),
        ('PSU', 'PSU'),
        ('Case', 'Case'),
    ])
    image = models.ImageField(upload_to='guides/images/')

    def __str__(self):
        return f"{self.component} Image for {self.guide.title}"