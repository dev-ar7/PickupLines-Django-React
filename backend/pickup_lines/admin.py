from django.contrib import admin
from django.contrib.auth.models import Group
from .models import PickupLines



admin.site.register(PickupLines)
admin.site.unregister(Group)


admin.site.site_header = "Pickup-Lines Admin"
admin.site.index_title = "Welcome to Pickup-Lines"
admin.site.site_title = "Pickup-Lines"