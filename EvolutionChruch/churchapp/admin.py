from django.contrib import admin
from .forms import PersonForm
from .models import Person 

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('person_email', 'person_fname', 'person_lname',)
    form = PersonForm
    
class Meta:
    model = Person

admin.site.register(Person, PersonAdmin)
