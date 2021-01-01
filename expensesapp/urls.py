from django.urls import path,include
from .views import *

urlpatterns = [

    path('',home,name='home'),
    path('add',add_expenses,name='add_expenses'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup',signup)
    
]

