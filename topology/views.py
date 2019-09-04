from django.shortcuts import render
from django.http.response import JsonResponse


def dash(request):
    return render(request, 'mytopology/index.html')


def topo(request):
    data = {
        "nodes": [
            {
                "id": 0,
                "name": "A",
                "typ" : "switch",  
            },
            {
                "id": 1,
                "name": "B",
                "typ" : "router",
            },
            {
                "id": 2,
                "name": "C",
                "typ" : "switch",
            },],
        "links": [
            {
                "source": 0,
                "target": 1
            },
            {
                "source": 0,
                "target": 2
            }]
    };
    response = JsonResponse(data, safe=False)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response
