from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


admin.site.register(User)


 
# class CustomUserAdmin(UserAdmin):
#    add_form = UserCreationForm
 
  
#    list_display = ('email', 'is_admin')
#    list_filter = ('is_admin',)
#    fieldsets = (
#        (None, {'fields': ('email', 'password')}),
#        ('Permissions', {'fields': ('is_admin',)}),
#    )
#    add_fieldsets = (
#        (None, {
#            'classes': ('wide',),
#            'fields': ('email','password1', 'password2'),
#        }),
#    )
#    ordering = ('email',)
#    filter_horizontal = ()
 
 
# # Now register the new UserAdmin...
# admin.site.register(User, CustomUserAdmin)

 
