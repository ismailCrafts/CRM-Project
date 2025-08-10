from django.contrib import admin
from crmapp.models import Customers

# Register your models here.
class customer_admin(admin.ModelAdmin):
        list_display = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'city',
        'created_at',
    )


admin.site.register(Customers, customer_admin)