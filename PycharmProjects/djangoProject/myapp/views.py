
from datetime import datetime
from django.shortcuts import render
# Create your views here.
def home(request):
    context={'time':datetime.now()}
    return render(request, 'myapp/homepage.html', context=context)
