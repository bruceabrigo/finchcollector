from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Finch, Toy
from .forms import FeedingForm

# create dumby finch data in a python list 
# # These will not be saved to a database, but will be used for reference to verify functionality

# finches = [
#     {'scientific_name': 'European Goldfinch', 'color': 'brown and white', 'description': 'small bird, got some rad colors', 'cluster_size': 2},
#     {'scientific_name': 'Hawkfin', 'color': 'Orange, brown, and white', 'description': 'small bird, looks like an orange creamcicle lowkey', 'cluster_size': 4},
# ]

# Create your views here.

# render a home page view
def home(request):
    # take a request, and render a view
    return render(request, 'home.html')

# render an about about page view
def about(request):
    # take a request, and render a view
    return render(request, 'about.html')
    
def finch_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finch_detail(request, finch_id):
    # take in a finch_id from the param
    # create sql get request to define and GET finch_id
    # after GET, render a single finch by its ID
    finch = Finch.objects.get(id=finch_id)
    # from our form import, we need to include the Feeding Form
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form
    })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    # we only want certain fields
    fields = ['color', 'description']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

def add_feeding(request, finch_id):
    # define form from Feeding Form
    form = FeedingForm(request.POST)
    # check if form is valid
    if form.is_valid():
        # save feeding to the finch id
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

# define a toy class
class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

class ToyDetail(DeleteView):
    model = Toy
    template_name = 'toys/detail.html'

class ToyCreate(CreateView):
    model = Toy
    fields = ['name','color']

    def form_valid(self, form):
        # this will act as our validation check
        # the super func allows for the original inherited CreateView func to work as intended
        return super().form_valid(form)
    
class ToyUpdate(UpdateView):
    model = Toy
    field = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'