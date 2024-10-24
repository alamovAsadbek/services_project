from django.shortcuts import render
from django.views import View

from home.views import BaseView
from services.models import ServiceModel
from team.models import ReviewModel


class ServicesView(BaseView):
    def get(self, request):
        context = self.get_context_data()

        service = ServiceModel.objects.filter(is_active=True)
        review = ReviewModel.objects.all()

        context['services'] = service
        context['reviews'] = review
        return render(request, 'service.html', context)


class WorksView(View):
    def get(self, request):
        return render(request, 'blog.html')
