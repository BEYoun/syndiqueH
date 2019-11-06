from django.shortcuts import render
from Residence.forms import SondageForm 
import string,random,datetime
from django.conf import settings
from .models import sondage,reponseSondage,assemblee,alerte
from Accounts.models import Batiment,Profil,Appartement
from utils.function import sendMail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Syndics.models import accHabitant
from Habitant.models import cotisationValidation
from Residence.models import alerte,cotisation,ordreAssemblee,evenement
from django.contrib.auth.models import User
mois = {
            "January":"01", "February":"02","March":"03","April":"04","May":"05","June":"06","July":"07","August":"08","September":"09","October":"10","November":"11","December":"08"
        }
# Create your views here.
@login_required(login_url="/accounts/login/")
def home(request,id_batiment):
    bat = Batiment.objects.get(pk=id_batiment)
    cotis = cotisation.objects.all().filter(batiment=bat)
    apparts = Appartement.objects.all().filter(batiment=bat)
    return render(request, 'residance/home.html', {'id_batiment':id_batiment,'batiment':bat,"residants":cotis,"apprtements":apparts})
@login_required(login_url="/accounts/login/")
def email(request,id_batiment):
    bat = Batiment.objects.get(pk=id_batiment)
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'residance/email.html', {'id_batiment':id_batiment,'batiment':bat})
@login_required(login_url="/accounts/login/")
def todo(request,id_batiment):
    bat = Batiment.objects.get(pk=id_batiment)
    ass = assemblee.objects.all().filter(batiment=bat)
    if request.method == 'POST':
        
        tab = request.POST.get('date').split(",")
        tab[0]=mois[tab[0]]
        nouvelleAssemble = assemblee(titre=request.POST.get('title'),batiment=bat,description=request.POST.get('description'),type_ass=request.POST.get('type'),date=datetime.datetime.strptime(tab[0]+"-"+tab[1]+"-"+tab[2], "%m- %d- %Y"))
        nouvelleAssemble.save()
        print(datetime.datetime.strptime(tab[0]+"-"+tab[1]+"-"+tab[2], "%m- %d- %Y"))
    return render(request, 'residance/todo.html', {'id_batiment':id_batiment,'batiment':bat,"assemblees":ass})
@login_required(login_url="/accounts/login/")
def chat(request,id_batiment):
    bat = Batiment.objects.get(pk=id_batiment)
    
    return render(request, 'residance/chats.html', {'id_batiment':id_batiment,'batiment':bat})
@login_required(login_url="/accounts/login/")
def calendrier(request,id_batiment):
    bat = Batiment.objects.get(pk=id_batiment)
    try:
        events = evenement.objects.all().filter(batiment=bat)
        print(events)
    except:
        events = None
    if request.method == 'POST':
        print(request.POST)
        tab = request.POST.get('date_debut').split(",")
        tab[0]=mois[tab[0]]
        tab2 = request.POST.get('date_fin').split(",")
        tab2[0]=mois[tab2[0]]
        newEv = evenement(Titre=request.POST.get('titre_evenement'),
            batiment=bat,
            type_evenement=request.POST.get('typeEv'),
            date_debut=datetime.datetime.strptime(tab[0]+"-"+tab[1]+"-"+tab[2], "%m- %d- %Y"),
            date_fin=datetime.datetime.strptime(tab2[0]+"-"+tab2[1]+"-"+tab2[2], "%m- %d- %Y"),
            description=request.POST.get('description'))
        newEv.save()
    return render(request, 'residance/calendrier.html', {'id_batiment':id_batiment,'batiment':bat,'evenements':events})
@login_required(login_url="/accounts/login/")
def newSondage(request,id_batiment):
    bat = Batiment.objects.get(pk=id_batiment)
    sondages= sondage.objects.all().filter(batiment=bat)
    if request.method == 'POST':
        form = SondageForm(request.POST)
        newS = sondage(question=request.POST.get('question'),content=request.POST.get('content'),batiment=bat,finSondage=datetime.datetime.strptime(request.POST.get('finSondage_submit'), "%d/%m/%Y"))
        newS.save()
        rep1=reponseSondage(rep=request.POST.get('rep1'),sondage=newS)
        rep1.save()
        rep2=reponseSondage(rep=request.POST.get('rep2'),sondage=newS)
        rep2.save()
        if request.POST.get('rep3') :
            rep3=reponseSondage(rep=request.POST.get('rep3'),sondage=newS)
            rep3.save()
        if request.POST.get('rep4') :
            rep4=reponseSondage(rep=request.POST.get('rep4'),sondage=newS)
            rep4.save()
    else:
        form = SondageForm()
    return render(request, 'residance/newSondage.html', {'form':form,'id_batiment':id_batiment,'sondages':sondages,'batiment':bat})
@login_required(login_url="/accounts/login/")
def alertez(request,id_batiment):
    bat = Batiment.objects.get(pk=id_batiment)
    try:
        alertes = alerte.objects.all().filter(batiment=bat)
        print(alertes)
    except:
        alertes = None
    return render(request, 'residance/alerte.html', {'alertes':alertes,'id_batiment':id_batiment,'batiment':bat})
@login_required(login_url="/accounts/login/")
def cotisationx(request,id_batiment):
    bat = Batiment.objects.get(pk=id_batiment)
    users = Profil.objects.all().filter(batiment=bat)
    return render(request, 'residance/cotisation.html', {'users':users,'id_batiment':id_batiment,'batiment':bat})
@login_required(login_url="/accounts/login/")
def viewCotisation(request,id_batiment,id_habitant):
    bat = Batiment.objects.get(pk=id_batiment)
    user = User.objects.get(pk=id_habitant)
    try:
        cotis = cotisation.objects.all().filter(habitant=user)
    except:
        cotis = None
    try:
        cotisV = cotisationValidation.objects.all().filter(batiment=bat,user=user)
    except:
        cotisV = None
    return render(request, 'residance/viewCotisation.html', {'user':user,'id_batiment':id_batiment,'cotisations':cotis,'batiment':bat,'cotisationsV':cotisV})
    
@login_required(login_url="/accounts/login/")
def viewSondage(request,id_batiment):
    bat = Batiment.objects.get(pk=id_batiment)
    sondages= sondage.objects.all().filter(batiment=bat)
    viewS=None
    comments=None
    if request.method == 'POST':
        viewS= sondage.objects.get(pk=request.POST.get('id_sondage'))
        comments = reponseSondage.objects.all().filter(sondage=viewS)
        print(comments)
    return render(request, 'residance/viewSondage.html', {'sondages':sondages,'id_batiment':id_batiment,'batiment':bat,'viewS':viewS,"comments":comments})
@login_required(login_url="/accounts/login/")
def document(request,id_batiment):
    if request.method == 'POST':
        pass
    return render(request, 'residance/document.html', locals())

@login_required(login_url="/accounts/login/")
def newHabitant(request,id_batiment):
    bat = Batiment.objects.get(pk=id_batiment)
    apparts = Appartement.objects.all().filter(batiment=bat)

    if request.method == "POST":
        try:
            acc = accHabitant.objects.create(email=request.POST.get('email'),firstName=request.POST.get('name'))
            subject = "incription plateform"
            from_email = settings.EMAIL_HOST_USER
            to_email = []
            to_email.append(request.POST.get('email'))
            signup_message = """ Bonjour Mr {0},\n \n Merci pour votre inscritpion, vueillez remplir le formulaire suivant pour vous inscrire en tant que habitant votre inscription : 
            \thttp://127.0.0.1:8000/accounts/creationHabitant/{1}/{2}/{3}
            """.format(request.POST.get('name'),acc.id,id_batiment,request.POST.get('appart'))
            sendMail(subject=subject,from_email=from_email,to_email=to_email,signup_message=signup_message)
        except:
            messages.error(request, "duplicate email.")
        users = User.objects.all()

    else:
        users = User.objects.all()
        print(request.user)
    return render(request, 'residance/newAcc.html', {'users':users,'batiment':bat,'id_batiment':id_batiment,'appartements':apparts})

@login_required(login_url="/accounts/login/")
def detailAssemblee(request,id_batiment,id_assemble):
    ass = assemblee.objects.get(pk=id_assemble)
    ordre = None
    try:
        ordre = ordreAssemblee.objects.all().filter(ass=ass)
    except:
        print('error')
    if request.method == 'POST':
        ordreAssemblee(question=request.POST.get('ordre'),ass=ass).save()
    return render(request, 'residance/detailAss.html', {"assemblees":ass,'id_batiment':id_batiment,'id_assemble':id_assemble,'ordre':ordre})
@login_required(login_url="/accounts/login/")
def viewAssemblee(request,id_batiment,id_assemble):
    ass = assemblee.objects.get(pk=id_assemble)
    try:
        ordre = ordreAssemblee.objects.all().filter(ass=ass)
    except:
        print('error')
    return render(request, 'pdf/process.html', {"assemblees":ass,'id_batiment':id_batiment,'id_assemble':id_assemble,'ordre':ordre})