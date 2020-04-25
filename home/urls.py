# DJANGO
from django.urls import path

# APPS
from home import views

urlpatterns = [
    path(route='',
         name='homepage',
         view=views.HomePageView.as_view())
]
