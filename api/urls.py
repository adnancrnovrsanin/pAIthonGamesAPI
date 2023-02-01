from django.urls import path
from . import views

urlpatterns = [
    path('aki', views.getAgentPathAki),
    path('jocke', views.getAgentPathJocke),
    path('draza', views.getAgentPathDraza),
    path('bole', views.getAgentPathBole),
    path('single/start', views.startingBoard),
    path('single/ai', views.aiMove),
    path('loosers', views.checkLoosers),
]