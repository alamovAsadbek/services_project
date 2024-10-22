from django.shortcuts import render
from django.views import View

from social_network.models import SiteModel


class FooterView(View):
    def __init__(self, navigate_link):
        super().__init__()
        self.navigate_link = navigate_link

    def get_context(self):
        footer_information = SiteModel.objects.all()
        return {
            'footer_information': footer_information
        }


class HomeView(View):
    def get(self, request):
        footer_view = FooterView(navigate_link='home')
        footer_context = footer_view.get_context()

        site_information = SiteModel.objects.all()
        context = {
            'site_information': site_information,
            **footer_context,
        }

        return render(request, 'index.html', context)
