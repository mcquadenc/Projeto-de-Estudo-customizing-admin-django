# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoDocumento'
        db.create_table('documentos_tipodocumento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('documentos', ['TipoDocumento'])

        # Adding model 'Documento'
        db.create_table('documentos_documento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('descricap', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documentos.TipoDocumento'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ano', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('endereco', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('data_cadastro', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('documentos', ['Documento'])


    def backwards(self, orm):
        # Deleting model 'TipoDocumento'
        db.delete_table('documentos_tipodocumento')

        # Deleting model 'Documento'
        db.delete_table('documentos_documento')


    models = {
        'documentos.documento': {
            'Meta': {'object_name': 'Documento'},
            'ano': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'data_cadastro': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'descricap': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'endereco': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documentos.TipoDocumento']"})
        },
        'documentos.tipodocumento': {
            'Meta': {'object_name': 'TipoDocumento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['documentos']