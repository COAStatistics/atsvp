from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('background/', views.background, name='background'),
    path('glossary/', views.glossary, name='glossary'),
    path('download/', views.download, name='download'),
    path('documentation/', views.documentation, name='documentation'),
    path('quickfacts/', views.quickfacts, name='quick facts')
]
