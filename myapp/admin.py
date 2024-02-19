from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tour, TourCategory, Review, Booking, User
# Register your models here.
admin.site.register(Tour)
admin.site.register(TourCategory)
admin.site.register(Review)
admin.site.register(Booking)
admin.site.register(User)