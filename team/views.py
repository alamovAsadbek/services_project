from django.shortcuts import render

from home.views import BaseView


class ContactView(BaseView):
    def get(self, request):
        context = self.get_context_data()
        return render(request, 'contact.html', context)
