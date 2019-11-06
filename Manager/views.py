from django.shortcuts import render
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
    user = User.objects.get(pk=id_syndique)
    if request.method == "POST":
        user.is_active=True
        user.save()
        subject = "incription plateform"
        from_email = settings.EMAIL_HOST_USER
        to_email = []
        to_email.append(user.email)
        signup_message = """ Bonjour Mr {0},\n \n Vos information on etez validé, vueillez remplir le formulaire suivant concernant les information sur votre batiment : 
        \thttp://127.0.0.1:8000/accounts/infoBati/{1}
        """.format(user.last_name,user.id)
        sendMail(subject=subject,from_email=from_email,to_email=to_email,signup_message=signup_message)
    return render(request, 'manager/viewNewAcc.html', {'user':user})
