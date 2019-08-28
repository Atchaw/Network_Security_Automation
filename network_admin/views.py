from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from layer2 import views


@login_required
def dashboard(request):
    #views.connect(request)
    return render(request, 'dashboard.html', {'section': 'dashboard'})
