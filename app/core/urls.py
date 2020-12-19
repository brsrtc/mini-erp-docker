# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

from django.urls import path, re_path, include
from . import views


urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),

    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # add this
    path('company/', include('company.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('order-item/', include('order_item.urls')),
    path('address/', include('address.urls')),
    # The home page
]