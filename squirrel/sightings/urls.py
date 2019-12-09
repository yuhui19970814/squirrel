from django.urls import path
  
from . import views
urlpatterns = [
    path('', views.all_squirrels),
    path('add/', views.add_squirrels),
    path('<unique_squirrel_id>/', views.update_squirrels),
    path('sightings/stats/',views.stats),
]

