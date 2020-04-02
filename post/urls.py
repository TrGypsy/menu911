from django.urls import path
from .views import *


urlpatterns = [
    path('about/', post_about, name='about'),
    path('<int:id>/', post_detaiL, name="detail"),
    
]
