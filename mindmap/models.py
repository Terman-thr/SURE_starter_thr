from django.db import models


# Create your models here.
class Node(models.Model):
    """
    Record nodes in different map.

    Num is used for identify the node.
    """
    id = models.AutoField(primary_key=True)
    mapid = models.IntegerField()
    num = models.IntegerField(default=0)
    content = models.CharField(max_length=200)
    positionx = models.IntegerField()
    positiony = models.IntegerField()


class Relation(models.Model):
    """Relationship between nodes."""
    id = models.AutoField(primary_key=True)
    mapid = models.IntegerField()
    parent = models.IntegerField()
    child = models.IntegerField()


class Maps(models.Model):
    id = models.AutoField(primary_key=True)
    mapname = models.CharField(max_length=200)
