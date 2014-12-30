from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms
from deathvalleydogs.models import Trip, Hike, Dog, Rig, Writeup, Quote

class DogAdminForm(forms.ModelForm):
    fields = ("name", "ham", "active", "birth_date", "family", "known_for")
    trips = forms.ModelMultipleChoiceField(
        queryset=Trip.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name='Trips',
            is_stacked=False
        )
    )

    class Meta:
        model = Dog

    def __init__(self, *args, **kwargs):
        super(DogAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['trips'].initial = self.instance.trips.all()

    def save(self, commit=True):
        dog = super(DogAdminForm, self).save(commit=False)

        if commit:
          dog.save()

        if dog.pk:
          dog.trips = self.cleaned_data['trips']
          self.save_m2m()

        return dog


class DogAdmin(admin.ModelAdmin):
    form = DogAdminForm

class TripAdmin(admin.ModelAdmin):
    filter_horizontal = ('dogs', 'rigs')

class HikeAdmin(admin.ModelAdmin):
    filter_horizontal = ('dogs',)

admin.site.register(Trip, TripAdmin)
admin.site.register(Hike, HikeAdmin)
admin.site.register(Dog, DogAdmin)
admin.site.register(Rig)
admin.site.register(Writeup)
admin.site.register(Quote)

