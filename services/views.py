from django.shortcuts import render
from django.views import View

from home.views import BaseView


class ServicesView(BaseView):
    def get(self, request):
        context = self.get_context_data()
        return render(request, 'service.html', context)


class WorksView(View):
    def get(self, request):
        return render(request, 'blog.html')
