from django.contrib import admin
from .models import Partners


class PartnersAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'manager_name', "manager_approve", 'CEO_approve')

    def partner_info(self, obj):
        return obj.description


admin.site.register(Partners, PartnersAdmin)

