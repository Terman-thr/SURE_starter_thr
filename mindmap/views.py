from django.shortcuts import render
from .models import Node, Relation


def get_index(request):
    db_reset()
    # Get all nodes
    nodes = Node.objects.all()
    relation = Relation.objects.all()
    # Loop through the nodes and print the contents
    # for node in nodes:
    #     print(node.id)
    return render(request, 'index.html', {'nodes': nodes, 'relations': relation})


def db_reset():
    Node.objects.all().delete()
    node1 = Node.objects.create(content='node 1', positionx=50, positiony=50)
    node2 = Node.objects.create(content='node 2', positionx=360, positiony=150)
    node3 = Node.objects.create(content='node 2', positionx=50, positiony=300)
    node1.save()
    node2.save()
    node3.save()
    nodes = Node.objects.all()
    relation = Relation.objects.create(parent=nodes[0].id, child=nodes[1].id)
    relation.save()
