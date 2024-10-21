from django.shortcuts import render
from django.views import View

from social_network.models import SiteModel


class FooterView(View):
    def __init__(self, navigate_link):
        super().__init__()
        self.navigate_link = navigate_link

    def get(self, request):
        footer_information = SiteModel.objects.all()
        context = {
            'footer_information': footer_information
        }
        print(context)
        return render(request, 'layouts/copyright/copyright.html', context)


class HomeView(View):
    def get(self, request):
        site_information = SiteModel.objects.all()
        context = {
            'site_information': site_information
        }
        FooterView.as_view()
        return render(request, 'index.html', context)
