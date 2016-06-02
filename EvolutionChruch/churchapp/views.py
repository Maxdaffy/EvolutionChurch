from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime

from .forms import ContactForm, PersonForm

# Create your views here.

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')

def person(request):
    title = 'Bienvenido  a su sistema de gestion de iglesias'
    if request.user.is_authenticated():
        title = "Welcome Back Mr. %s" %(request.user)
        user = "%s" %(request.user)
        
        #add form
        form = PersonForm(request.POST or None)

        context = {
            "template_title": title, 
            "template_user": user,  
            "form": form, 
        }

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()       
            #try:
            subject = 'Prueba de Correo Python'
            message = 'Nuestro primer Correo desde una aplicacion de Python'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, 'ingmaxseipio@gmail.com']

            send_mail(subject, message, from_email, to_email, fail_silently=False)
        #    except BadHeaderError:
        #        return HttpResponse('Invalid header found.')
        #    return HttpResponseRedirect('/contact/thanks/')
        #else:
        #    # In reality we'd use a form class
        #    # to get proper validation errors.
        #    return HttpResponse('Make sure all fields are entered and valid.')

            context = {
                "template_title": "Usuario Agregado Sastifactoriamente !!!!",         
            }
    
        return render(request,'Index.html', context)

def contact(request):
    form = ContactForm(request.POST or  None)
    context = {
        "form": form,
    }
    return render(request, "pages-login.html", context)
