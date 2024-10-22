from django.shortcuts import render
from django.views import View

from .models import AboutUsModel


class AboutView(View):
    def get(self, request):
        about = AboutUsModel.objects.all()
        context = {
            'about': about
        }
        return render(request, 'about.html', context)
