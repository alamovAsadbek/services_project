from django.shortcuts import render

from home.views import BaseView
from services.models import FeatureModel
from team.models import TeamModel
from .models import AboutUsModel


class AboutView(BaseView):
    def get(self, request):
        context = self.get_context_data()

        about = AboutUsModel.objects.all()
        featured_service = FeatureModel.objects.filter(is_active=True)
        team = TeamModel.objects.all()

        context['about'] = about
        context['featured_service'] = featured_service
        context['team'] = team
        
        return render(request, 'about.html', context)
