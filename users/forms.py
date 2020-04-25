# DJANGO
from django import forms
from django.contrib.auth.models import User

# APPS
from users.models import Profile

class SignUpForm(forms.Form):
    
    username = forms.CharField(min_length=4, 
                               max_length=50,
                               required=True)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )
    
    codeUTEC = forms.CharField(max_length=10, required=True)

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username
    
    def clean_email(self):
        """Email must be unique."""
        email = self.cleaned_data['email']

        if email[-11:] != 'utec.edu.pe':
            raise forms.ValidationError('Introduce a UTEC email.')

        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('Email is already in use.')
        return email

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        codeUTEC = data['codeUTEC']
        data.pop('codeUTEC')
        user = User.objects.create_user(**data)

        #creating profile
        profile = Profile(user=user, codeUTEC=codeUTEC)
        profile.save()




    # Profile

