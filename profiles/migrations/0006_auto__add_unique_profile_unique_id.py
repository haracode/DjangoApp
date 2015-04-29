# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Profile', fields ['unique_id']
        db.create_unique(u'profiles_profile', ['unique_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Profile', fields ['unique_id']
        db.delete_unique(u'profiles_profile', ['unique_id'])


    models = {
        u'profiles.profile': {
            'Meta': {'unique_together': "(('email', 'unique_id'),)", 'object_name': 'Profile'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'0:0:0'", 'max_length': '120'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'unique_id': ('django.db.models.fields.CharField', [], {'default': "'0000'", 'unique': 'True', 'max_length': '120'}),
            'update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['profiles']