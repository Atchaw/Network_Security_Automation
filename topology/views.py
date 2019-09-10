from django.shortcuts import render
from django.http.response import JsonResponse 
from layer2.models import Device
import json

def dash(request):
    return render(request, 'mytopology/index.html')


def topo(request):
    nbDevice = Device.objects.count()
    device = Device.objects.all()

    nodes = []       
    typ = ""
    for d in device:
        if d.hostname.startswith('s'):
            typ = "switch"
        else:
            typ = "router"
        node = {}
        node["id"] = d.hostname
        node["name"] = d.hostname
        node["typ"] = typ
        nodes.append(node)
      
    links = []
    for d in device:
        link = {}
        link["source"] = d.hostname
        link["target"] = d.description
        links.append(link)
    
    visualization_dict={}
    visualization_dict["nodes"] = nodes
    visualization_dict["links"] = links
    
    print(visualization_dict)
    print('------------------------------')
    print(json.dumps(visualization_dict))
    data = visualization_dict
    

    response = JsonResponse(data, safe=False)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response
