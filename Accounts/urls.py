from django.urls import path, re_path
from django.conf.urls import url
from . import views
app_name = 'accounts'
urlpatterns = [
    url(r'^login/$',views.login,name="login"),
    url(r'^register/$',views.signup,name="signup"),
    url(r'^logout/$',views.logout_view,name="logout"),
    url('^creationSyndique/(?P<id_syndique>\d+)/$',views.creationSyndique,name="creationSyndique"),
    url('^creationHabitant/(?P<id_compt>\d+)/(?P<id_batiment>\d+)/(?P<id_appartement>\d+)$',views.creationHabitant,name="newHabitant"),
    # re_path(r'^connexion$', views.connexion, name='connexion'),
]