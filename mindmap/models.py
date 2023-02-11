from django.db import models


# Create your models here.
class Node(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200)
    positionx = models.IntegerField()
    positiony = models.IntegerField()


class Relation(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.IntegerField()
    child = models.IntegerField()
