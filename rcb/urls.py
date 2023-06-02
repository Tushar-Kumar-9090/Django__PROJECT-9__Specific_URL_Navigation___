from django.urls import path
from rcb.views import *
app_name = 'rcb'
urlpatterns = [
    path('virat_strings/', virat_strings, name='virat_strings'),

    path('virat/', virat, name='virat'),
]