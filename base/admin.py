from django.contrib import admin
from .models import Donation, DonatedPeople, DonationAutherization, ClientMessages

admin.site.register(DonatedPeople)
admin.site.register(Donation)
admin.site.register(DonationAutherization)
admin.site.register(ClientMessages  )