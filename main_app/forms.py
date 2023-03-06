# import ModelForm from django forms
from django.forms import ModelForm
# import feeding model for feeding form
from .models import Feeding

# create form class
class FeedingForm(ModelForm):
  class Meta:
    # model will be equal to the feeding model
    model = Feeding
    # add form fields
    fields = ['date', 'meal']
