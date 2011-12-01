# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'HikeWriteup'
        db.delete_table('data_hikewriteup')


    def backwards(self, orm):
        
        # Adding model 'HikeWriteup'
        db.create_table('data_hikewriteup', (
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('hike', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Hike'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('short_desc', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('dog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Dog'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('data', ['HikeWriteup'])


    models = {
        'data.dog': {
            'Meta': {'object_name': 'Dog'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'family': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ham': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'known_for': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        'data.hike': {
            'Meta': {'object_name': 'Hike'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'dogs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data.Dog']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map_points': ('django.db.models.fields.TextField', [], {'default': "'<kml></kml>'", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'trip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Trip']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        'data.quote': {
            'Meta': {'object_name': 'Quote'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        'data.rig': {
            'Meta': {'object_name': 'Rig'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'dog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Dog']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'data.trip': {
            'Meta': {'object_name': 'Trip'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'dogs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data.Dog']", 'symmetrical': 'False'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map_points': ('django.db.models.fields.TextField', [], {'default': "'<kml></kml>'", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rigs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data.Rig']", 'symmetrical': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        'data.writeup': {
            'Meta': {'object_name': 'Writeup'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'dog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Dog']"}),
            'hike': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Hike']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'short_desc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'trip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Trip']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['data']
