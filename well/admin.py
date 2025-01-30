from django.contrib import admin
from well.models import *
from unfold.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(Wells)
class WellsAdminClass(ModelAdmin):
    pass


@admin.register(Tubular)
class TubularAdminClass(ModelAdmin):
    pass

@admin.register(TubularTemp)
class TubularTempAdminClass(ModelAdmin):
    pass

@admin.register(TubeConnection)
class TubeConnectionAdminClass(ModelAdmin):
    pass


@admin.register(Country)
class CountryAdminClass(ModelAdmin):
    pass

@admin.register(Fields)
class FieldsAdminClass(ModelAdmin):
    pass

@admin.register(Reservoirs)
class ReservoirsAdminClass(ModelAdmin):
    pass


