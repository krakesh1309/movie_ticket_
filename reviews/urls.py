from django.urls import path 
from . import views 

urlpatterns = [
    path('add-review/<slug>/',views.add_review,name='add_review')
]