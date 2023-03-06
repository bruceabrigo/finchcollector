from django.contrib import admin

# Register your models here.
from .models import Finch, Feeding, Toy

admin.site.register(Finch)
# register Feeding to admin site
admin.site.register(Feeding)
# register Toy to admin to admin site
admin.site.register(Toy)