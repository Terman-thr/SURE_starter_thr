import json
from django.shortcuts import render
from .models import Node, Relation
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


def get_index(request):
    #db_reset()
    # Get all nodes
    nodes = Node.objects.all()
    relation = Relation.objects.all()
    # Loop through the nodes and print the contents
    # for node in nodes:
    #     print(node.id)
    return render(request, 'index.html', {'nodes': nodes, 'relations': relation})


@csrf_exempt
def save_api(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        # rewrite the database and restart id from 1
        Node.objects.all().delete()
        Relation.objects.all().delete()
        cursor = connection.cursor()
        cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'mindmap_node'")
        cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'mindmap_relation'")
        for node in data["nodes"]:
            new_node = Node(num=int(node['id']), positionx=node['positionx'],
                            positiony=node['positiony'], content=node['content'])
            new_node.save()
        for relation in data["relation"]:
            new_relation = Relation(parent=relation['from'], child=relation['to'])
            new_relation.save()



        return JsonResponse({'status': 'success'})


def db_reset():
    Node.objects.all().delete()
    Relation.objects.all().delete()
    node1 = Node.objects.create(num=1, content='node 1', positionx=50, positiony=50)
    node2 = Node.objects.create(num=2, content='node 2', positionx=360, positiony=150)
    node3 = Node.objects.create(num=3, content='node 3', positionx=50, positiony=300)
    node1.save()
    node2.save()
    node3.save()
    nodes = Node.objects.all()
    relation = Relation.objects.create(parent=nodes[0].id, child=nodes[1].id)
    relation.save()
