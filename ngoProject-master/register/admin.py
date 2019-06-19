from django.contrib import admin
from .models import Register, Registration


class RegistrationInline(admin.TabularInline):
    model = Registration
    raw_id_fields = ['event']


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'adult_qty',
                    'child_qty', 'created', 'updated']
    list_filter = [ 'created', 'updated']
    inlines = [RegistrationInline]
    
admin.site.register(Register, RegisterAdmin)
