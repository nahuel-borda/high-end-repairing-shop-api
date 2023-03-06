from django.contrib import admin
from autocompletefilter.admin import AutocompleteFilterMixin
from autocompletefilter.filters import AutocompleteListFilter
from .models import (
    Client,
    Device,
    Brand,
    Model,
    Part,
    Service,
    Operator,
    Provider
)
from django import forms

class ServiceModelForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Service
        fields = "__all__"


@admin.register(Provider)
class ProviderAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("name", "address", "celphone", "email")
    search_fields = ("name", "address", "celphone", "email")


@admin.register(Client)
class ClientAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("firstname", "lastname", "personal_id", "celphone", "email")
    search_fields = ("firstname", "lastname", "personal_id", "celphone", "email")


@admin.register(Device)
class DeviceAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("patent", "model", "brand", "client")
    search_fields = ("patent", "model", "brand", "client")
    list_filter = (
            ("model", AutocompleteListFilter),
            ("brand", AutocompleteListFilter),
            ("client", AutocompleteListFilter),
        )

    autocomplete_fields = ["model", "brand", "client"]


@admin.register(Part)
class PartAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("name", "price", "provider")
    search_fields = ("name", "price", "provider")
    list_filter = (
            ("provider", AutocompleteListFilter),
        )

    autocomplete_fields = ["provider"]


@admin.register(Operator)
class OperatorAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("firstname", "lastname", "personal_id", "celphone", "email")
    search_fields = ("firstname", "lastname", "personal_id", "celphone", "email")


@admin.register(Service)
class ServiceAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("device", "status", "ingress_date", "start_date", "end_date", "operator", "description")
    search_fields = ("device", "status", "ingress_date", "start_date", "end_date", "operator", "description")
    #list_filter = (
    #        ("parts", AutocompleteListFilter),
    #    )

    form = ServiceModelForm
    #readonly_fields = ("status", "ingress_date")

    autocomplete_fields = ["parts"]


@admin.register(Brand)
class BrandAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Model)
class ModelAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
