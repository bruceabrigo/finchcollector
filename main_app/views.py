from django.shortcuts import render

from .models import Finch

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