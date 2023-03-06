from django.db import models
from django.urls import reverse
from datetime import date

# define the MEALS choices globally
MEALS = (
    # create a 2-tuple for each choice
    # first item in 2-tuple represents where it will be stored in the database
    # second 2-tuple represents what will be returned from the database.
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Finch(models.Model):
    # each item below represents at definition for each element that belongs to a finch,
    # s_name is scientific name
    s_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.s_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id })
    
    # now, I am going to represent a one-to-many relationship.
# Add new Feeding model below Finch model
    
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        # add the choices field
        choices = MEALS,
        # set a default value for the meal to be 'B'
        default = MEALS[0][0]
    )
    # add finch foreign key reference
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        # this method is coming from django
        # produced like this: get_<name_of_field>_display()
        return f"{self.get_meal_display()} on {self.date}"
    
    # change the default sort
    class Meta:
        ordering = ['-date']
    