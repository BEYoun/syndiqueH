from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from Accounts.models import Profil,Batiment,Appartement, newAcc
from Accounts.forms import SignUpForm, SyndiqueForm
from Commercial.models import accSyndic
from Syndics.models import accHabitant
# Create your views here.

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user= form.get_user()
            auth_login(request,user)
            if user.profil.role == 'CM':
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('commercial:home')
            elif user.profil.role == 'SY':
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('syndique:home')
            elif user.profil.role == 'MA':
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('manager:home')
            elif user.profil.role == 'HP':
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('habitant:maResidance')
        else:
            messages.error(request, "Invalid username or password.")
            
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', { 'form':form })

def logout_view(request):
    logout(request)
    return redirect('accueil:home')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profil.role = Profil.COMMERCIAL
            user.save()
            return redirect('accounts:login')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', locals())

def creationSyndique(request,id_syndique):
    info = newAcc.objects.get(pk=id_syndique)
    if request.method == 'POST':
        form = SyndiqueForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.refresh_from_db()  # load the profile instance created by the signal
            # user.profil.role = Profil.SYNDIQUE
            Profil(user=user,role="SY",batiment=Batiment.objects.get(pk=1),appartement=Appartement.objects.get(pk=1)).save()
            messages.success(request, "Votre compt va etre verifier par un de Manager un mail vous sera envoyer dici peu a tre bien tot")
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('accounts:login')
    else:
        form = SyndiqueForm()
    return render(request, 'registration/comptSyndique.html', {"info":info,'form':form})

def creationHabitant(request,id_compt,id_batiment,id_appartement):
    info = accHabitant.objects.get(pk=id_compt)
    bat = Batiment.objects.get(pk=id_batiment)
    app = Appartement.objects.get(pk=id_appartement)
    print(info)
    if request.method == 'POST':
        form = SyndiqueForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profil.role = Profil.HABITANTP
            app.user=user
            app.save()
            user.profil.appartement = app
            user.save()
            messages.success(request, "Votre compt a bien ete creer vueillez vous connectez")
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('accounts:login')
    else:
        form = SyndiqueForm()
    return render(request, 'registration/comptHabitant.html', {"info":info,'form':form,'bat':bat,"app":app})