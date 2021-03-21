from django.urls import path
from .views import *

app_name = 'profile'

urlpatterns = [
    path('', ProfileHome.as_view(), name='home'),
    path('create/', CreateProfile.as_view(), name='create-profile'),
    path('<str:pk>/update/', UpdateProfile.as_view(), name='update-profile'),
]
