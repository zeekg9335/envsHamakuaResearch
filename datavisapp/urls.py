from django.urls import path
from . import views


urlpatterns = [
    path('', views.about ),
    path('about/', views.about ),
    path('hamakua-data/', views.hamakuaData, name='hamakuaData'),
    path('hamakua-data/', views.afterDisking, name='afterhamakuaData'),
    path('hamakua-information/', views.hamakuaInformation, name='hamakuaInformation'),
    path('hamakua-inhabitants/', views.hamakuaInhabitants, name='hamakuaInhabitants'),
    path('hamakua-afterdisking/', views.afterDisking, name='afterhamakuaData')

    
]