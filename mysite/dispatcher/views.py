from msilib.schema import Feature
from django.shortcuts import render
from django.http import HttpResponse
from .models import Trailer, Features, TrailerInstance, Producer
from django.views import generic
from django.shortcuts import render, get_object_or_404

def index(request):
    
    
    num_trailers = Trailer.objects.all().count()
    num_instances = TrailerInstance.objects.all().count()
    
    
    num_instances_available = TrailerInstance.objects.filter(status__exact='rea').count()
    
     
    num_features = Features.objects.count()
    
    
    context = {
        'num_trailers': num_trailers,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_features': num_features,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)

def features(request):
    
    features = Features.objects.all()
    context = {
        'features': features
    }
    print(features)
    return render(request, 'features.html', context=context)


def feature(request, feature_id):
    single_feature = get_object_or_404(Feature, pk=feature_id)
    return render(request, 'feature.html', {'feature': single_feature})


class TrailerListView(generic.ListView):
    model = Trailer
    template_name = 'trailer_list.html'

class TrailerDetailView(generic.DetailView):
    model = Trailer
    template_name = 'trailer_detail.html'