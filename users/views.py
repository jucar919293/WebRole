# Django
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

# APPS
from users.forms import SignUpForm
from users.models import Profile

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['carrera', 'phoneNumber', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('home:homepage')
    #    return reverse('users:detail', kwargs={'username': username})


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('home:homepage')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'


class LogoutView(auth_views.LogoutView, LoginRequiredMixin):
    """Logout view."""

    template_name = 'users/logged_out.html'
    
