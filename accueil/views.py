from django.shortcuts import render,redirect
from Accounts.models import newAcc
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'accueil/index.html', locals())
def blog(request):
    return render(request, 'accueil/blog.html', locals())
def blogV(request):
    return render(request, 'accueil/blog-view.html', locals())
def about(request):
    return render(request, 'accueil/about.html', locals())
def contact(request):
    return render(request, 'accueil/contact.html', locals())
def demandeDemo(request):
    if request.POST:
        print(request.POST)
        newAc = newAcc(nom=request.POST.get('nom'),
                    prenom = request.POST.get('prenom'),
                    email = request.POST.get('email'),
                    numero = request.POST.get('numero'),
                    typeClient = request.POST.get('type')
                    # ville = request.POST.get('next'),
                    # address = request.POST.get('next'),
                    # quartier = request.POST.get('next')
                    )
        newAc.save()
        messages.success(request, "Vos informations vont être verifier par un de nos managers un mail vous sera envoyé d'ici peu a trés vite.")
    return redirect('accueil:home')