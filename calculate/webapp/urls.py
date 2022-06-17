from django.urls import path

from webapp.views import calculate_page, home_page

urlpatterns = [
    path('', home_page),
    path('calculate/', calculate_page),
]