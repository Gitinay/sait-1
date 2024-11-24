from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=64)
    sostav = models.CharField(max_length=256)
    image = models.ImageField(null=False)

    def __str__(self):
        return f"Название бургера {self.name}"