from django.contrib import admin
from autocompletefilter.admin import AutocompleteFilterMixin
from autocompletefilter.filters import AutocompleteListFilter
from .models import (
    Cliente,
    Moto,
    Marca,
    Modelo,
    Repuesto,
    Servicio,
    Mecanico,
    Proveedor
)
from django import forms

class ServicioModelForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Servicio
        fields = "__all__"


@admin.register(Proveedor)
class ProveedorAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("name", "direccion", "telefono", "email")
    search_fields = ("name", "direccion", "telefono", "email")


@admin.register(Cliente)
class ClienteAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("dni", "numero_celular", "email", "nombre", "apellido")
    search_fields = ("dni", "numero_celular", "email", "nombre", "apellido")


@admin.register(Moto)
class MotoAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("patente", "modelo", "marca", "cliente")
    search_fields = ("patente", "modelo", "marca", "cliente")
    list_filter = (
            ("modelo", AutocompleteListFilter),
            ("marca", AutocompleteListFilter),
            ("cliente", AutocompleteListFilter),
        )

    autocomplete_fields = ["modelo", "marca", "cliente"]


@admin.register(Repuesto)
class RepuestoAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("nombre", "costo", "proveedor")
    search_fields = ("nombre", "costo", "proveedor")
    list_filter = (
            ("proveedor", AutocompleteListFilter),
        )

    autocomplete_fields = ["proveedor"]


@admin.register(Mecanico)
class MecanicoAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("nombre", "apellido", "dni", "numero_celular", "email")
    search_fields = ("nombre", "apellido", "dni", "numero_celular", "email")


@admin.register(Servicio)
class ServicioAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("moto", "estado", "fecha_ingreso", "fecha_inicio", "fecha_fin")
    search_fields = ("moto", "estado", "fecha_ingreso", "fecha_inicio", "fecha_fin", "respuestos")
    list_filter = (
            ("moto", AutocompleteListFilter),
            ("respuestos", AutocompleteListFilter),
        )

    form = ServicioModelForm
    readonly_fields = ('estado', "fecha_ingreso", "fecha_inicio", "fecha_fin")

    autocomplete_fields = ["moto", "respuestos"]


@admin.register(Marca)
class MarcaAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Modelo)
class ModeloAdmin(AutocompleteFilterMixin, admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
