from django.contrib import admin
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile admin """
    list_display = ('pk', 'user', 'codeUTEC',
                    'nTokens', 'typeMember', 
                    'carrera','picture')
    
    list_display_links = ('pk','user','codeUTEC')
    list_editable = ('nTokens', 'typeMember',
                     'carrera')
    
    readonlyfields = ('created','modified')


class ProfileInLine(admin.StackedInline):
    """ Profile in-line admin users """
    
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """ Adding profile admin to base user admin"""

    inlines=(ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
