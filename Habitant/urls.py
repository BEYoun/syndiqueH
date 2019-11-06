from django.urls import path, re_path
from django.conf.urls import url
from . import views
app_name = 'habitant'
urlpatterns = [
    path('home', views.home,name="home"),
    url('email', views.email,name="email"),
    url('todo', views.todo,name="todo"),
    url('chat', views.chat,name="chat"),
    url('calendrier', views.calendrier,name="calendrier"),
    path('profil', views.profil,name="profil"),
    path('maResidance', views.maResidance,name="maResidance"),
    path('monAppart', views.monAppart,name="monAppart"),
    path('cotisation', views.cotisation,name="cotisation"),
    path('sondage', views.sondagex,name="sondage"),
    url('^viewSondage/(?P<id_sondage>\d+)/$',views.viewSondage,name="viewSondage"),
    url('^vote/(?P<id_sondage>\d+)/(?P<id_comm>\d+)/$',views.vote,name="vote"),
    path('AlerteIncident', views.AlerteIncident,name="AlerteIncident"),
    path('ContactUrgence', views.ContactUrgence,name="ContactUrgence"),
]