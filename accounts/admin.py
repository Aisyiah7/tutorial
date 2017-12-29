from django.contrib import admin
from accounts.models import UserProfile

# Register your models here.

#admin.site.site_header = 'Administration'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'phone', 'website')

    #change name from description --> user_info
    def user_info(self, obj):
        return obj.description

    #customise object sort order
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone')
        return queryset

    #shorten the column name
    user_info.short_description = 'Info'

admin.site.register(UserProfile, UserProfileAdmin)
