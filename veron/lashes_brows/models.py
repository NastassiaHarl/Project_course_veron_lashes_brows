from django.db import models

class Master(models.Model):
    name = models.CharField(max_length=255)
    info_of_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    photo = models.ImageField()
    master = models.ForeignKey(Master, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo

class Address(models.Model):
    photo_map = models.ImageField()
    info_address = models.CharField(max_length=255)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo_map

class Service(models.Model):
    name_service = models.CharField(max_length=255)
    info_service = models.CharField(max_length=255)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_service

class Review(models.Model):
    text = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Price(models.Model):
    price = models.IntegerField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.price


class Gift_certificate(models.Model):
    photo_certificate = models.ImageField()
    stock = models.CharField(max_length=255)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)

    def __str__(self):
        return self.photo_certificate