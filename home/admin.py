from django.contrib import admin

from .models import *

admin.site.site_header = 'EcoGaz Admin'
admin.site.site_title = 'EcoGaz Admin Portal'
admin.site.index_title = 'Xush Kelibsiz EcoGaz Admin Portal ga'
admin.site.register(BaseCarouselModel)
