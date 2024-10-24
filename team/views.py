from django.shortcuts import render

from home.views import BaseView


class ContactView(BaseView):
    def get(self, request):
        contex = self.get_context_data()
        return render(request, 'contact.html', contex)
