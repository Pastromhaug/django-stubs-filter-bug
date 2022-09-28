from django.db import models

class Cheese(models.Model):
    a = models.BooleanField()

def f() -> None:
    Cheese.objects.filter(field=True).filter(field2=True)
    qs = Cheese.objects.all()
    qs.filter(field=True)
