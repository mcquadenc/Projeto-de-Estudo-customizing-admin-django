# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Documento, TipoDocumento
from admin_filters import TipoDocumento as FilterTipoDocumento

class DocumentoAdmin(admin.ModelAdmin):
    list_filter = (FilterTipoDocumento,)
    list_display = ('nome', 'numero','ano','tipo', 'user')
    exclude = ['user',]

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()
    
    def queryset(self, request):
        qs = super(DocumentoAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        user = request.user

        if db_field.name == "tipo":
            kwargs["queryset"] = TipoDocumento.objects.filter(groups__in = user.groups.all())
            return db_field.formfield(**kwargs)
        return super(DocumentoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug',)

admin.site.register(Documento, DocumentoAdmin)
admin.site.register(TipoDocumento)
