from django.contrib import admin

from .models import PersonalProfile


@admin.register(PersonalProfile)
class PersonalProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "name": ("name",),
    }
