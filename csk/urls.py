from django.urls import path
from csk.views import *
app_name = 'csk'
urlpatterns = [
    path('dhoni_strings/', dhoni_strings, name='dhoni_strings'),
    path('dhoni/', dhoni, name='dhoni'),
]