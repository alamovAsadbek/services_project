from django.shortcuts import render
from django.views import View

from about_us.models import AboutUsModel
from services.models import ServiceModel, FeatureModel
from social_network.models import SiteModel
from .models import BaseCarouselModel


class BaseView(View):
    def get_context_data(self):
        site_information = SiteModel.objects.all()
        carousel_information = BaseCarouselModel.objects.all()
        return {
            'site_information': site_information,
            'carousel_information': carousel_information
        }

    def get(self, request):
        context = self.get_context_data()
        return render(request, 'layouts/base/base.html', context)


class HomeView(BaseView):
    def get(self, request):
        context = self.get_context_data()
        about = AboutUsModel.objects.all()
        service = ServiceModel.objects.filter(is_active=True)
        featured_service = FeatureModel.objects.filter(is_active=True)
        context['services'] = service
        context['about'] = about
        context['featured_service'] = featured_service
        return render(request, 'index.html', context)
