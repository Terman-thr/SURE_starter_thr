import json
from django.shortcuts import render
from .models import Node, Relation, Maps
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


def get_index(request):
    """Render the index page."""
    maps = Maps.objects.all()
    return render(request, 'index.html', {'maps': maps})


@csrf_exempt
def create_map(request):
    """Create a new map and return new map id."""

    if request.method == 'POST':
        # Get the map name from the request
        data = json.loads(request.body.decode('utf-8'))
        map_name = data['mapName']
        # Create a new map in the database
        new_map = Maps.objects.create(mapname=map_name)
        # Return a JSON response with the new map number
        response_data = {'mapNum': new_map.id}
        return JsonResponse(response_data)


def get_map(request, id):
    """Render different map requests."""
    nodes = Node.objects.filter(mapid=id)
    relation = Relation.objects.filter(mapid=id)
    mapname = Maps.objects.get(id=id).mapname
    return render(request, 'map.html', {'nodes': nodes, 'relations': relation, 'mapid': id, 'mapname': mapname})


@csrf_exempt
def save_api(request, mapid):
    """
    Handle request from index.html.

    Save nodes and their relationship into db.sqlite3.

    Turn off csrf token authorization.

    """
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        # rewrite the database and restart id from 1
        Node.objects.filter(mapid=mapid).delete()
        Relation.objects.filter(mapid=mapid).delete()
        cursor = connection.cursor()
        # cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'mindmap_node'")
        # cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'mindmap_relation'")

        # Insert nodes and relation into database
        for node in data["nodes"]:
            new_node = Node(mapid=mapid, num=int(node['id']), positionx=node['positionx'],
                            positiony=node['positiony'], content=node['content'])
            new_node.save()
        for relation in data["relation"]:
            new_relation = Relation(mapid=mapid, parent=relation['from'], child=relation['to'])
            new_relation.save()
        return JsonResponse({'status': 'success'})


def db_reset():
    """Test, reset database as three nodes and one relation."""
    Node.objects.all().delete()
    Relation.objects.all().delete()
    node1 = Node.objects.create(num=1, content='node 1', positionx=50, positiony=50)
    node2 = Node.objects.create(num=2, content='node 2', positionx=360, positiony=150)
    node3 = Node.objects.create(num=3, content='node 3', positionx=50, positiony=300)
    node1.save()
    node2.save()
    node3.save()
    nodes = Node.objects.all()
    relation = Relation.objects.create(parent=nodes[0].num, child=nodes[1].num)
    relation.save()
