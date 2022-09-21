from django.contrib import admin  
from django.urls import path  
from CricketLiveScores import views  

urlpatterns = [  
    path('player', views.player),  
    path('show',views.show),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
    path('play',views.playgame),
    path('scores',views.scores,name="scores"),
] 