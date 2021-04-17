from django.contrib import admin
from.models import (
    Client,
    Admin,
    Book,
    Transfer,
    TransferRequest
)

# Register your models here.
admin.site.register(Client)
admin.site.register(Admin)
admin.site.register(Book)
admin.site.register(Transfer)
admin.site.register(TransferRequest)


