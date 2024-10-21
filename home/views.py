from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class ServicesView(View):
    def get(self, request):
        return render(request, 'service.html')
