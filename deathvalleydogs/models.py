from django.db import models
from datetime import datetime


class ModelBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True, default=datetime.now)

    class Meta:
        abstract = True


class Dog(ModelBase):
    name = models.CharField(max_length=200)
    ham = models.CharField(max_length=200)
    active = models.BooleanField()
    birth_date = models.DateField('birth date', null=True)
    family = models.CharField(max_length=20)
    known_for = models.CharField(max_length=300, blank=True)

    class Meta:
        db_table = 'data_dog'

    def __unicode__(self):
        return self.name


class Rig(ModelBase):
    dog = models.ForeignKey(Dog)
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    active = models.BooleanField()

    class Meta:
        db_table = 'data_rig'

    def __unicode__(self):
        return self.name


class Trip(ModelBase):
    dogs = models.ManyToManyField(Dog)
    rigs = models.ManyToManyField(Rig)
    name = models.CharField(max_length=200)
    date = models.DateField()
    end_date = models.DateField(null=True)
    map_points = models.TextField(null=True, default="<kml></kml>")

    class Meta:
        db_table = 'data_trip'

    def __unicode__(self):
        return self.name


class Hike(ModelBase):
    trip = models.ForeignKey(Trip)
    dogs = models.ManyToManyField(Dog)
    name = models.CharField(max_length=200)
    date = models.DateField()
    map_points = models.TextField(null=True, default="<kml></kml>")

    class Meta:
        db_table = 'data_hike'

    def __unicode__(self):
        return self.name


class Writeup(ModelBase):
    dog = models.ForeignKey(Dog)
    trip = models.ForeignKey(Trip)
    hike = models.ForeignKey(Hike, blank=True, null=True)
    name = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=200)
    body = models.TextField()

    class Meta:
        db_table = 'data_writeup'

    def __unicode__(self):
        return self.name


class Quote(ModelBase):
    quote = models.TextField()
    credit = models.CharField(max_length=40)

    class Meta:
        db_table = 'data_quote'

    def __unicode__(self):
        return self.quote
