from django.shortcuts import render
from django.views import View

from home.models import BaseCarouselModel
from social_network.models import SiteModel


class BaseView(View):
    def get(self, request):
        site_information = SiteModel.objects.all()
        carousel_information = BaseCarouselModel.objects.all()
        context = {
            'site_information': site_information,
            'carousel_information': carousel_information
        }
        print(carousel_information)
        return render(request, 'layouts/base/base.html', context)


class HomeView(BaseView):
    def get(self, request):
        site_information = SiteModel.objects.all()
        context = {
            'site_information': site_information,
        }
        return render(request, 'index.html', context)
