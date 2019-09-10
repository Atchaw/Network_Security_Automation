from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from layer2 import views
from layer2.models import Switch
from layer3.models import Router

@login_required
def dashboard(request):
    router = Router.objects.count()
    switch = Switch.objects.count()
    return render(request, 'dashboard.html', {'section': 'dashboard', 'router': router, "switch": switch})

def connect(request):
    views.connect(request)
