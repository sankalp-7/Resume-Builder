from django.urls import path
from.views import home,builder
app_name='resume'

urlpatterns=[ 
    path('',home,name='home'),
    path('builder/',builder,name='builder')
]