from django.db import models


class Cheese(models.Model):
    a = models.TextField()
    b = models.BooleanField()


def f() -> None:
    Cheese.objects.filter(blablable=True)
    qs = Cheese.objects.all()
    qs.filter(wawawa=True)
