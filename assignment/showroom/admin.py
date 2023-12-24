from django.contrib import admin

from showroom.models import Brand, Car, Comment, Transaction

# Register your models here.

admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(Transaction)
admin.site.register(Comment)
