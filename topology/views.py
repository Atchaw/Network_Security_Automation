from django.shortcuts import render
from django.http import JsonResponse


def dash(request):
    return render(request, 'mytopology/index.html')


def topo(request):
    data = {
        "nodes": [
            {
                "id": 0,
                "name": "A",
                
            },
            {
                "id": 1,
                "name": "B"
            },
            {
                "id": 2,
                "name": "C",
            },
        ],
        "links": [
            {
                "id": 0,
                "source": 0,
                "target": 1
            },
             {
                "id": 1,
                "source": 0,
                "target": 2
            }
        ]
    };
    return JsonResponse(data, safe=False)
