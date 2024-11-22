from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# class DoctorsAdmin(admin.ModelAdmin):
#     list_display = ["user"]

# admin.site.register(Doctors, DoctorsAdmin)
admin.site.register(Doctors)

admin.site.register(Policy)


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "middle_name"]


admin.site.register(User, UserAdmin)

# ----------
admin.site.register(Specialization)


admin.site.register(DoctorsReviews)


admin.site.register(Institution)


admin.site.register(Direction)


admin.site.register(FilePDF)


admin.site.register(ResearchResults)


admin.site.register(Records)
