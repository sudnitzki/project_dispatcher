from msilib.schema import Feature
from django.shortcuts import render
from django.http import HttpResponse
from .models import Trailer, Features, TrailerInstance, Producer
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    
    
    num_trailers = Trailer.objects.all().count()
    num_instances = TrailerInstance.objects.all().count()
    num_instances_available = TrailerInstance.objects.filter(status__exact='rea').count()  
    num_producer = Producer.objects.count()
    
    
    context = {
        'num_trailers': num_trailers,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_producer': num_producer,
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
    single_feature = get_object_or_404(Features, pk=feature_id)
    return render(request, 'feature.html', {'feature': single_feature})


def search(request):

    query = request.GET.get('query')
    query_filter = Q(type__icontains=query) | Q(summary__icontains=query)
    search_results = Trailer.objects.filter(query_filter)
    return render(request, 'search.html', {'trailers': search_results, 'query': query})


class TrailerListView(generic.ListView):
    model = Trailer
    paginate_by = 2
    template_name = 'trailer_list.html'

class TrailerDetailView(generic.DetailView):
    model = Trailer
    template_name = 'trailer_detail.html'