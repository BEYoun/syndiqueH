from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'syndique'
urlpatterns = [
    path('home', views.home,name="home"),
    path('email', views.email,name="email"),
    path('chat', views.chat,name="chat"),
    path('todo', views.todo,name="todo"),
    path('calendrier', views.calendrier,name="calendrier"),
    path('NewClient', views.newHabitant,name="newHabitant"),
    path('NewResidence', views.newResidance,name="newResidance"),
    path('Sondage', views.Sondage,name="Sondage"),
    path('usagers', views.usagers,name="usagers"),
    path('Paiement', views.Paiement,name="Paiement"),
    path('password', views.password,name="password"),
    path('viewResidance', views.viewResidance,name="viewResidance"),
    path('profil', views.profil,name="profil"),
    url('^importFichier/(?P<id_batiment>\d+)/$',views.importFichier,name="importFichier"),
]