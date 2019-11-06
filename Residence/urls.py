from django.urls import path, re_path
from django.conf.urls import url
from . import views
app_name = 'residance'
urlpatterns = [
    url('^(?P<id_batiment>\d+)/email$', views.email,name="email"),
    url('^(?P<id_batiment>\d+)/todo$', views.todo,name="todo"),
    url('^(?P<id_batiment>\d+)/chat$', views.chat,name="chat"),
    url('^(?P<id_batiment>\d+)/calendrier$', views.calendrier,name="calendrier"),
    url('^(?P<id_batiment>\d+)/home$',views.home,name="home"),
    url('^(?P<id_batiment>\d+)/newSondage$',views.newSondage,name="newSondage"),
    url('^(?P<id_batiment>\d+)/viewSondage$',views.viewSondage,name="viewSondage"),
    url('^(?P<id_batiment>\d+)/alerte$',views.alertez,name="alerte"),
    url('^(?P<id_batiment>\d+)/cotisation$',views.cotisationx,name="cotisation"),
    url('^(?P<id_batiment>\d+)/cotisation/(?P<id_habitant>\d+)$',views.viewCotisation,name="viewCotisation"),
    url('^(?P<id_batiment>\d+)/newHab$',views.newHabitant,name="newHab"),
    url('^(?P<id_batiment>\d+)/document$',views.document,name="document"),
    url('^(?P<id_batiment>\d+)/detailAssemblee/(?P<id_assemble>\d+)/$', views.detailAssemblee,name="detailAssemblee"),
    url('^(?P<id_batiment>\d+)/viewAssemblee/(?P<id_assemble>\d+)/$', views.viewAssemblee,name="viewAssemblee"),
    # re_path(r'^connexion$', views.connexion, name='connexion'),
]