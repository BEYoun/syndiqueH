from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'accueil'
urlpatterns = [
    path('', views.home,name="home"),   
    path('blog', views.blog,name="blog"),   
    path('blog-view-article', views.blogV,name="blogView"),   
    path('about', views.about,name="about"),   
    path('contact', views.contact,name="contact"),
    path('demande-demo', views.demandeDemo,name="demandeDemo"),
]