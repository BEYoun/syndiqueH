from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from Syndics.models import accHabitant,Email_envoi,Email_recep
from django.conf import settings
from django.contrib import messages
from utils.function import sendMail
from django.contrib.auth.decorators import login_required
from Syndics.forms import BatimentForm,DocForm
from Accounts.models import Batiment,Profil,Appartement
from Residence.models import assemblee
# Create your views here.
@login_required(login_url="/accounts/login/")
def home(request):
    emails = Email_recep.objects.all().filter(from_email=request.user)
    return render(request, 'syndique/home.html', {"emails":emails})
@login_required(login_url="/accounts/login/")
def email(request):
    batiments = Batiment.objects.all().filter(user=request.user)
    usagers = []
    try:
        emails = Email_recep.objects.all().filter(from_email=request.user)
    except :
        emails = None
    for batiment in batiments:
        habitants = Profil.objects.all().filter(batiment=batiment)
        for habitant in habitants:
            if habitant not in usagers:
                usagers.append(habitant.user)
    if request.method == 'POST':
        if request.POST.get('id_user') == '0':
            messages.error(request, "Veuillez indiquez a qui envoier le message")
            return redirect('syndique:email')
        user = User.objects.get(pk=request.POST.get('id_user'))
        em = Email_envoi(To=user,cc=request.POST.get('CC'),subject=request.POST.get('Subject'),message=request.POST.get('message'))
        em.save()
        em_recep =Email_recep(emails=em,from_email=request.user)
        em_recep.save()
    return render(request, 'syndique/email.html', {"usagers":usagers,"emails":emails})
@login_required(login_url="/accounts/login/")
def profil(request):
    return render(request, 'syndique/profil.html', locals())
@login_required(login_url="/accounts/login/")
def Sondage(request):
    return render(request, 'syndique/sondage.html', locals())
@login_required(login_url="/accounts/login/")
def todo(request):
    ass = assemblee.objects.all()
    return render(request, 'syndique/todo.html', {"assemblees":ass})

@login_required(login_url="/accounts/login/")
def Paiement(request):
    batiments = Batiment.objects.all().filter(user=request.user)
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'syndique/Paiement.html', {"batiments":batiments})
@login_required(login_url="/accounts/login/")
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('syndique:home')
        else:
            return redirect('/syndique/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'syndique/password.html', {"forms":forms})
@login_required(login_url="/accounts/login/")
def usagers(request):
    batiments = Batiment.objects.all().filter(user=request.user)
    usagers = []
    for batiment in batiments:
        habitants = Profil.objects.all().filter(batiment=batiment)
        for habitant in habitants:
            if habitant not in usagers:
                usagers.append(habitant.user)
    return render(request, 'syndique/usagers.html', locals())
@login_required(login_url="/accounts/login/")
def chat(request):
    return render(request, 'syndique/chats.html', locals())
@login_required(login_url="/accounts/login/")
def calendrier(request):
    batiments = Batiment.objects.all().filter(user=request.user)
    assemblees = []
    for batiment in batiments:
        try:
            assembl = assemblee.objects.all().filter(batiment=batiment)
        except:
            assembl = None
        if assembl:
            for x in assembl:
                assemblees.append(x)
    return render(request, 'syndique/calendrier.html', {"assemblees":assemblees})
@login_required(login_url="/accounts/login/")
def newHabitant(request):
    if request.method == "POST":
        try:
            acc = accHabitant.objects.create(email=request.POST.get('email'),firstName=request.POST.get('name'))
            subject = "incription plateform"
            from_email = settings.EMAIL_HOST_USER
            to_email = []
            to_email.append(request.POST.get('email'))
            
            signup_message = """ Bonjour Mr {0},\n \n Merci pour votre inscritpion, vueillez remplir le formulaire suivant pour vous inscrire en tant que habitant votre inscription : 
            \thttp://127.0.0.1:8000/accounts/creationHabitant/{1}
            """.format(request.POST.get('name'),acc.id)
            sendMail(subject=subject,from_email=from_email,to_email=to_email,signup_message=signup_message)
        except:
            messages.error(request, "duplicate email.")
        # new = newAcc.objects.create(nom=request.POST.get('nom'),prenom=request.POST.get('prenom'),email=request.POST.get('email'),address=request.POST.get('address'),ville=request.POST.get('ville'),quartier=request.POST.get('quartier'))
        # # print(request.POST.get('nom'))
        # return render(request, 'commercial/importFileInformation.html', {"new":new})

    else:
        users = User.objects.all()
        print(request.user)
    return render(request, 'syndique/newAcc.html', {'users':users})
@login_required(login_url="/accounts/login/")
def newResidance(request):
    if request.method == 'POST':
        form = BatimentForm(request.POST)
        if form.is_valid():

            batiment = form.save()
            batiment.user = request.user
            batiment.save()
            for i in range(batiment.nbrApp):
                Appartement(nom=batiment.nom+"_"+str(i),nombreHabitant=3,batiment=batiment,etage=1).save()
                print(i)
            return redirect('syndique:viewResidance')
        
    else:
        form = BatimentForm()
    return render(request, 'syndique/newResidance.html', {'form':form})

@login_required(login_url="/accounts/login/")
def importFichier(request,id_batiment):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'syndique/chats.html', locals())
@login_required(login_url="/accounts/login/")
def viewResidance(request):
    batiments = Batiment.objects.all().filter(user=request.user)
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'syndique/viewResidance.html', {'batiments':batiments})