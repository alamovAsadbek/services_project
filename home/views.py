from django.shortcuts import render
from django.views import View

from social_network.models import SiteModel


class HomeView(View):
    def get(self, request):
        site_information = SiteModel.objects.all()
        context = {
            'site_information': site_information
        }
        return render(request, 'index.html', context)


class FooterView(View):
    def get(self, request):
        footer_information = SiteModel.objects.all()
        context = {
            'footer_information': footer_information
        }
        return render(request, 'layouts/copyright/copyright.html', context)
