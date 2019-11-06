from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'commercial'
urlpatterns = [
    path('home', views.home,name="home"),
    path('email', views.email,name="email"),
    path('todo', views.todo,name="todo"),
    path('chat', views.chat,name="chat"),
    path('calendrier', views.calendrier,name="calendrier"),
    path('NewClient', views.newClient,name="newClient"),
    path('profil', views.profil,name="profil"),
    # path('newAcc', views.newAccount,name="newAcc"),
    # url('^importFile/(?P<newAcc_id>\d+)/$', views.importFile,name="importFile"),
]