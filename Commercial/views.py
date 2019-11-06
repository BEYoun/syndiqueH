from django.shortcuts import render
from Accounts.models import newAcc
from django.conf import settings
from utils.function import sendMail
from django.contrib import messages
from Commercial.models import accSyndic
# Create your views here.
def home(request):
    return render(request, 'commercial/home.html', locals())
def email(request):
    return render(request, 'commercial/email.html', locals())
def todo(request):
    return render(request, 'commercial/todo.html', locals())
def chat(request):
    return render(request, 'commercial/chats.html', locals())
def calendrier(request):
    return render(request, 'commercial/calendrier.html', locals())
def profil(request):
    return render(request, 'manager/profil.html', locals())
def newClient(request):
    if request.method == "POST":
        try:
            acc = accSyndic.objects.create(email=request.POST.get('email'),firstName=request.POST.get('name'))
            subject = "incription plateform"
            from_email = settings.EMAIL_HOST_USER
            to_email = []
            to_email.append(request.POST.get('email'))
            
            signup_message = """ Bonjour Mr {0},\n \n Merci pour votre inscritpion, vueillez remplir le formulaire suivant pour demarer votre inscription : 
            \thttp://127.0.0.1:8000/accounts/creationSyndique/{1}
            """.format(request.POST.get('name'),acc.id)
            sendMail(subject=subject,from_email=from_email,to_email=to_email,signup_message=signup_message)
        except:
            messages.error(request, "duplicate email.")
        # new = newAcc.objects.create(nom=request.POST.get('nom'),prenom=request.POST.get('prenom'),email=request.POST.get('email'),address=request.POST.get('address'),ville=request.POST.get('ville'),quartier=request.POST.get('quartier'))
        # # print(request.POST.get('nom'))
        # return render(request, 'commercial/importFileInformation.html', {"new":new})

    else:
        print('pas')
    return render(request, 'commercial/newAcc.html', locals())
