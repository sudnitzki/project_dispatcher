from django.shortcuts import render
from django.http import HttpResponse
from .models import Trailer, Features, TrailerInstance, Producer



def index(request):
    
    
    num_trailers = Trailer.objects.all().count()
    num_instances = TrailerInstance.objects.all().count()
    
    
    num_instances_available = TrailerInstance.objects.filter(status__exact='g').count()
    
    # Kiek yra autorių    
    num_features = Features.objects.count()
    
    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_books': num_trailers,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_features,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)