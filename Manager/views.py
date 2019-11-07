from django.shortcuts import render,redirect
from Accounts.models import newAcc
from django.conf import settings
from utils.function import sendMail
from django.contrib import messages
from Commercial.models import accSyndic
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request, 'manager/home.html', locals())
def email(request):
    return render(request, 'manager/email.html', locals())
def todo(request):
    return render(request, 'manager/todo.html', locals())
def chat(request):
    return render(request, 'manager/chats.html', locals())
def calendrier(request):
    return render(request, 'manager/calendrier.html', locals())
def profil(request):
    return render(request, 'manager/profil.html', locals())
def newClient(request):
    users = newAcc.objects.all()
    print(request.user)
    return render(request, 'manager/newAcc.html', {'users':users})
def newC(request):
    users = User.objects.all()
    print(request.user)
    return render(request, 'manager/Client.html', {'users':users})
def viewNewAcc(request,id_syndique):
    user = newAcc.objects.get(pk=id_syndique)
    try:
        subject = "incription plateform"
        from_email = settings.EMAIL_HOST_USER
        to_email = []
        to_email.append(user.email)
        print("fhie")
        signup_message = """ Bonjour Mr {0},\n \n Merci pour votre inscritpion, vueillez remplir le formulaire suivant pour demarer votre inscription : 
        \thttp://127.0.0.1:8000/accounts/creationSyndique/{1}
        """.format(user.nom,user.id)
        sendMail(subject=subject,from_email=from_email,to_email=to_email,signup_message=signup_message)
    except:
        messages.error(request, "duplicate email.")
        print("fhie3")
    # new = newAcc.objects.create(nom=request.POST.get('nom'),prenom=request.POST.get('prenom'),email=request.POST.get('email'),address=request.POST.get('address'),ville=request.POST.get('ville'),quartier=request.POST.get('quartier'))
    # # print(request.POST.get('nom'))
    # return render(request, 'commercial/importFileInformation.html', {"new":new})
    return redirect('manager:newClient1')
