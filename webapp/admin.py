from django.contrib import admin
from webapp.models import *

class MemberAdmin(admin.ModelAdmin):
    list_display=['get_member_email','admin_privilege']
    search_field=['user__email']
    @admin.display(description='Member Email')
    def get_member_email(self, obj):
        return obj.user.email
    
admin.site.register(Member,MemberAdmin)