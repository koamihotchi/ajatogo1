from .import views
from django.urls import path
from .views import accueil
from .views import service1,service2,service3,blog,register,team,blogdetail,about
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('', views.accueil, name='accueil'),
    path('service1/', views.service1, name='service1'),
    path('service2/', views.service2, name='service2'),
    path('service3/', views.service3, name='service3'),
    path('blog/' , views.blog, name='blog'),
    path('register/', views.register, name='register'),
    path('team/', views.team, name='team'),
    path('blogdetail/', views.blogdetail, name='blogdetail'),
    path('accueil/', views.accueil, name='accueil'),
    path('about/', views.about, name='about'),

    



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
