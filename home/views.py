from django.shortcuts import render
from django.views import View

from social_network.models import SiteModel


class BaseView(View):
    def get(self, request):
        site_information = SiteModel.objects.all()
        context = {
            'site_information': site_information,
        }
        print(context)
        return render(request, 'layouts/base/base.html', context)


class HomeView(BaseView):
    def get(self, request):
        site_information = SiteModel.objects.all()
        context = {
            'site_information': site_information,
        }
        return render(request, 'index.html', context)
