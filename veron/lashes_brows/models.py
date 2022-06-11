from django.db import models

class Service(models.Model):
    name_service = models.CharField(max_length=255)
    info_service = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name_service

class Review(models.Model):
    text = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.text