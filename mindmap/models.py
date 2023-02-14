from django.db import models


# Create your models here.
class Node(models.Model):
    """Num is used for identify the node."""
    id = models.AutoField(primary_key=True)
    mapid = models.IntegerField()
    num = models.IntegerField(default=0)
    content = models.CharField(max_length=200)
    positionx = models.IntegerField()
    positiony = models.IntegerField()


class Relation(models.Model):
    id = models.AutoField(primary_key=True)
    mapid = models.IntegerField()
    parent = models.IntegerField()
    child = models.IntegerField()
