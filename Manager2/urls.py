from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'manager'
urlpatterns = [
    path('home', views.home,name="home"),
    path('email', views.email,name="email"),
    path('todo', views.todo,name="todo"),
    path('chat', views.chat,name="chat"),
    path('calendrier', views.calendrier,name="calendrier"),
    path('NewClient', views.newClient,name="newClient1"),
    path('nouveauClient', views.newC,name="nouveauClient"),
    path('profil', views.profil,name="profil"),
    url('^viewNewAcc/(?P<id_syndique>\d+)/$',views.viewNewAcc,name="viewNewAcc"),
    
]