from django.contrib import admin

# Register your models here.
from .models import Profile #in models look for a Class called Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["email", "last_name", "first_name", "timestamp"]
    #allows customization of the Admin
    class Meta:
        model = Profile

admin.site.register(Profile, ProfileAdmin)
