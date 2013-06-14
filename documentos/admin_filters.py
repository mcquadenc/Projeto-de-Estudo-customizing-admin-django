# -*- coding: utf-8 -*-
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _
from models import TipoDocumento as DbTipoDocumento
from django.contrib.auth.models import User

class TipoDocumento(SimpleListFilter):
    title = _('Tipo de Documento')
    parameter_name = 'tipo'

    def lookups(self, request, model_admin):

        user = request.user
        lista_de_tipos = []
        
        if request.user.is_superuser:
            lista_de_tipos = DbTipoDocumento.objects.all()
        else:
           lista_de_tipos = DbTipoDocumento.objects.filter(groups__in = user.groups.all())

        list_filter = [ (tipo.id, _(tipo.nome)) for tipo in lista_de_tipos ]
        list_filter = tuple(list_filter)

        return list_filter

    def queryset(self, request, queryset):
        
        if self.value() != None and self.value() != '':
            tipo = DbTipoDocumento.objects.filter(id=self.value())
            return queryset.filter( tipo = tipo )
        else:
            return queryset.all()