from django.contrib import admin

from .models import Box, Client, Lease, StoreHouse


admin.site.register(Box)
admin.site.register(Client)
admin.site.register(Lease)
admin.site.register(StoreHouse)
