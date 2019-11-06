from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import string,random,datetime
from Residence.models import sondage,reponseSondage
from Accounts.models import Batiment,Profil
from Syndics.models import accHabitant,Email_envoi,Email_recep
from django.contrib.auth.decorators import login_required
from .models import vote,cotisationValidation
import datetime
from Residence.models import assemblee,evenement,alerte
from django.contrib import messages
from Residence.forms import AlerteForm
# Create your views here.
mois = {
            "January":"01", "February":"02","March":"03","April":"04","May":"05","June":"06","July":"07","August":"08","September":"09","October":"10","November":"11","December":"08"
        }
@login_required(login_url="/accounts/login/")
def home(request):
    return render(request, 'habitant/home.html', locals())

@login_required(login_url="/accounts/login/")
def profil(request):
    return render(request, 'habitant/profil.html', locals())
@login_required(login_url="/accounts/login/")
def email(request):
    bat = request.user.profil.batiment
    user = request.user
    emails = Email_recep.objects.all().filter(from_email=user)
    usagers = Profil.objects.all().filter(batiment=bat)
    usagers=usagers.exclude(user=user)
    if request.method == 'POST':
        if request.POST.get('id_user') == '0':
            messages.error(request, "Veuillez indiquez a qui envoier le message")
            return redirect('habitant:email')
        user = User.objects.get(pk=request.POST.get('id_user'))
        em = Email_envoi(To=user,cc=request.POST.get('CC'),subject=request.POST.get('Subject'),message=request.POST.get('message'))
        em.save()
        em_recep =Email_recep(emails=em,from_email=request.user)
        em_recep.save()
    
    print(usagers)
    return render(request, 'habitant/email.html', {"usagers":usagers,"emails":emails})
@login_required(login_url="/accounts/login/")
def todo(request):
    bat = Batiment.objects.get(pk=request.user.profil.batiment.id)
    ass = assemblee.objects.all().filter(batiment=bat)
    
    return render(request, 'habitant/todo.html', {"assemblees":ass})
@login_required(login_url="/accounts/login/")
def calendrier(request):
    bat = Batiment.objects.get(pk=request.user.profil.batiment.id)
    try:
        events = evenement.objects.all().filter(batiment=bat)
        print(events)
    except:
        events = None
    return render(request, 'habitant/calendrier.html', {'evenements':events})
@login_required(login_url="/accounts/login/")
def AlerteIncident(request):
    bat = request.user.profil.batiment
    user = request.user.profil
    my_record = alerte(habitant=user,
            batiment=bat)
    try:
        alertes = alerte.objects.all().filter(batiment=bat)
        print(alertes)
    except:
        alertes = None
    if request.POST:
        form = AlerteForm(request.POST, instance=my_record)
        al = form.save()
    else:
        form = AlerteForm()
    return render(request, 'habitant/AlerteIncident.html', {"form":form,"alertes":alertes})
@login_required(login_url="/accounts/login/")
def ContactUrgence(request):
    return render(request, 'habitant/ContactUrgence.html', locals())
@login_required(login_url="/accounts/login/")
def chat(request):
    return render(request, 'habitant/chats.html', locals())
@login_required(login_url="/accounts/login/")
def maResidance(request):
    return render(request, 'habitant/maResidance.html', locals())

@login_required(login_url="/accounts/login/")
def monAppart(request):
    return render(request, 'habitant/monAppart.html', locals())
@login_required(login_url="/accounts/login/")
def cotisation(request):
    user=request.user
    bat = request.user.profil.batiment
    cotisations = cotisationValidation.objects.all().filter(user=user)
    print(cotisations)
    if request.method == 'POST':
        print(request.POST)
        tab = request.POST.get('date').split(",")
        tab[0]=mois[tab[0]]
        cotisationValidation(nom=request.user.last_name,
            prenom=request.user.first_name,
            date=datetime.datetime.strptime(tab[0]+"-"+tab[1]+"-"+tab[2], "%m- %d- %Y"),
            user=user,
            batiment=bat).save()
        messages.success(request, "Votre demande de paiement a bien éte envoié et sera traiter par votre syndique le plus vite possible")

    return render(request, 'habitant/cotisation.html', {"cotisations":cotisations})
@login_required(login_url="/accounts/login/")
def sondagex(request):
    bat = Batiment.objects.get(pk=request.user.profil.batiment.id)
    print(bat.id)
    sondages= sondage.objects.all().filter(batiment=bat)
    try:
        print(sondages)
    except :
        sondages=None
    return render(request, 'habitant/sondage.html', locals())
@login_required(login_url="/accounts/login/")
def viewSondage(request,id_sondage):
    viewS= sondage.objects.get(pk=id_sondage)
    comments = reponseSondage.objects.all().filter(sondage=viewS)
    
    return render(request, 'habitant/viewSondage.html', {'viewS':viewS,"comments":comments})
@login_required(login_url="/accounts/login/")
def vote(request,id_comm,id_sondage):
    viewS= sondage.objects.get(pk=id_sondage)
    
    comm= reponseSondage.objects.get(pk=id_comm)
    try:
        user = request.user.profil
        vote.objects.all().filter(sondage=viewS)
    except:
        user = request.user.profil
        print(user)
        # v=vote(sondage=viewS,user=user)
        # v.save()
        comm.nombreVote=comm.nombreVote+1
        comm.save()
    return redirect("habitant:viewSondage",id_sondage=id_sondage)