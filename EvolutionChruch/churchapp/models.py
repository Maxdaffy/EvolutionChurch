from django.db import models
from django.utils import timezone

# Create your models here.

class Person(models.Model):
    person_fname = models.CharField("Person Name", max_length=30)
    person_lname = models.CharField("Person Last Name", max_length=30)
    person_birthday = models.DateTimeField(default=timezone.now)
    person_email = models.CharField("Person Email", max_length=100)
    person_maritalstatus = models.CharField(max_length=2)
    #person_rol = models.IntegerField("Member Type")

    def __str__ (self):
        return '/%s/' % self.person_email

    def get_absolute_url (self):
        return '/churchapp/%s/' % self.id


# Table rol church members 
#class MemberType(models.Model):
#    member_name = models.CharField("Member Name", max_length=50)




 
