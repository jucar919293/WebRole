# Django
from django.urls import path

# APPS
from users import views


urlpatterns = [

    path(
        route='signup/',
        view=views.SignUpView.as_view(),
        name='signup'
    ),

    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),

    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),

    path(
        route='update/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update'
    ),
]
