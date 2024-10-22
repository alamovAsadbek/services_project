from django.shortcuts import render
from django.views import View

from home.views import BaseView
from .models import AboutUsModel


class AboutView(BaseView):
    def get(self, request):
        super().get(request)
        about = AboutUsModel.objects.all()
        context = {
            'about': about
        }
        return render(request, 'about.html', context)
