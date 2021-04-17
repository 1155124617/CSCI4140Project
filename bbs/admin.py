from django.contrib import admin
from.models import (
    Client,
    Admin,
    Book,
    Transfer,
    TransferRequest,
    Rental
)

# Register your models here.
admin.site.register(Client)
admin.site.register(Admin)
admin.site.register(Book)
admin.site.register(Transfer)
admin.site.register(TransferRequest)
admin.site.register(Rental)


from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }
