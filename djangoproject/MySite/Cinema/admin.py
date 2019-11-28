from django.contrib import admin
# Register your models here.

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(Movie)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

'''
admin.site.register(Article)
admin.site.register(Editor)
admin.site.register(Comment)
'''
# admin.site.register(ExampleModel)
