# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Quote.created_at'
        db.add_column('data_quote', 'created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True), keep_default=False)

        # Adding field 'Quote.updated_at'
        db.add_column('data_quote', 'updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True), keep_default=False)

        # Deleting field 'Trip.created'
        db.delete_column('data_trip', 'created')

        # Deleting field 'Trip.modified'
        db.delete_column('data_trip', 'modified')

        # Adding field 'Trip.created_at'
        db.add_column('data_trip', 'created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True), keep_default=False)

        # Adding field 'Trip.updated_at'
        db.add_column('data_trip', 'updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True), keep_default=False)

        # Deleting field 'Dog.created'
        db.delete_column('data_dog', 'created')

        # Deleting field 'Dog.modified'
        db.delete_column('data_dog', 'modified')

        # Adding field 'Dog.created_at'
        db.add_column('data_dog', 'created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True), keep_default=False)

        # Adding field 'Dog.updated_at'
        db.add_column('data_dog', 'updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True), keep_default=False)

        # Deleting field 'Rig.created'
        db.delete_column('data_rig', 'created')

        # Deleting field 'Rig.modified'
        db.delete_column('data_rig', 'modified')

        # Adding field 'Rig.created_at'
        db.add_column('data_rig', 'created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True), keep_default=False)

        # Adding field 'Rig.updated_at'
        db.add_column('data_rig', 'updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True), keep_default=False)

        # Deleting field 'Hike.created'
        db.delete_column('data_hike', 'created')

        # Deleting field 'Hike.modified'
        db.delete_column('data_hike', 'modified')

        # Adding field 'Hike.created_at'
        db.add_column('data_hike', 'created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True), keep_default=False)

        # Adding field 'Hike.updated_at'
        db.add_column('data_hike', 'updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True), keep_default=False)

        # Deleting field 'Writeup.created'
        db.delete_column('data_writeup', 'created')

        # Deleting field 'Writeup.modified'
        db.delete_column('data_writeup', 'modified')

        # Adding field 'Writeup.created_at'
        db.add_column('data_writeup', 'created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True), keep_default=False)

        # Adding field 'Writeup.updated_at'
        db.add_column('data_writeup', 'updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Quote.created_at'
        db.delete_column('data_quote', 'created_at')

        # Deleting field 'Quote.updated_at'
        db.delete_column('data_quote', 'updated_at')

        # Adding field 'Trip.created'
        db.add_column('data_trip', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 4, 15), blank=True), keep_default=False)

        # Adding field 'Trip.modified'
        db.add_column('data_trip', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 4, 15), blank=True), keep_default=False)

        # Deleting field 'Trip.created_at'
        db.delete_column('data_trip', 'created_at')

        # Deleting field 'Trip.updated_at'
        db.delete_column('data_trip', 'updated_at')

        # Adding field 'Dog.created'
        db.add_column('data_dog', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 4, 15), blank=True), keep_default=False)

        # Adding field 'Dog.modified'
        db.add_column('data_dog', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 4, 15), blank=True), keep_default=False)

        # Deleting field 'Dog.created_at'
        db.delete_column('data_dog', 'created_at')

        # Deleting field 'Dog.updated_at'
        db.delete_column('data_dog', 'updated_at')

        # Adding field 'Rig.created'
        db.add_column('data_rig', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 4, 15), blank=True), keep_default=False)

        # Adding field 'Rig.modified'
        db.add_column('data_rig', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 4, 15), blank=True), keep_default=False)

        # Deleting field 'Rig.created_at'
        db.delete_column('data_rig', 'created_at')

        # Deleting field 'Rig.updated_at'
        db.delete_column('data_rig', 'updated_at')

        # Adding field 'Hike.created'
        db.add_column('data_hike', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 4, 15), blank=True), keep_default=False)

        # Adding field 'Hike.modified'
        db.add_column('data_hike', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 4, 15), blank=True), keep_default=False)

        # Deleting field 'Hike.created_at'
        db.delete_column('data_hike', 'created_at')

        # Deleting field 'Hike.updated_at'
        db.delete_column('data_hike', 'updated_at')

        # Adding field 'Writeup.created'
        db.add_column('data_writeup', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 4, 15), blank=True), keep_default=False)

        # Adding field 'Writeup.modified'
        db.add_column('data_writeup', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 4, 15), blank=True), keep_default=False)

        # Deleting field 'Writeup.created_at'
        db.delete_column('data_writeup', 'created_at')

        # Deleting field 'Writeup.updated_at'
        db.delete_column('data_writeup', 'updated_at')


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
            'map_points': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map_points': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rigs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data.Rig']", 'symmetrical': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        'data.writeup': {
            'Meta': {'object_name': 'Writeup'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'dog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Dog']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'short_desc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'trip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Trip']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['data']
