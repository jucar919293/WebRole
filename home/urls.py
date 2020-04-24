# DJANGO
from django.urls import path

# APPS
from home import views

urlpatterns = [
    path(route='',
         name='home',
         view=views.HomePageView.as_view())
]
