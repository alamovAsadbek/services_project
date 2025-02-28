from django.urls import path

from about_us.views import *
from home.views import *
from services.views import *
from team.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('works/', WorksView.as_view(), name='works'),
    path('contact/', ContactView.as_view(), name='contact'),
]

handler404 = 'home.views.handler404'
