from msilib.schema import Feature
from django.shortcuts import render
from django.http import HttpResponse
from .models import Trailer, Features, TrailerInstance, Producer
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

def index(request):
    
    
    num_trailers = Trailer.objects.all().count()
    num_instances = TrailerInstance.objects.all().count()
    num_instances_available = TrailerInstance.objects.filter(status__exact='tri').count()  
    num_free = num_trailers - num_instances_available
    
    
    context = {
        'num_trailers': num_trailers,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_free': num_free,
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

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = TrailerInstance
    template_name ='user_trailers.html'
    paginate_by = 10
    
    def get_queryset(self):
        return TrailerInstance.objects.filter(company=self.request.user).filter(status__exact='tri').order_by('dexpected_return')


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.error(request, f'Urer name {username} already exists!')
                return redirect('register')
            else:

                if User.objects.filter(email=email).exists():
                    messages.error(request, f'email {email} already exists!')
                    return redirect('register')
                else:
                   
                    User.objects.create_user(username=username, email=email, password=password)
        else:
            messages.error(request, 'error password!')
            return redirect('register')
    return render(request, 'register.html')