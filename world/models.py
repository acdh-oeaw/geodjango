from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from django.contrib.postgres.fields import HStoreField
from datetime import datetime
from .validators import date_validator
import re
# automatically genereated by
# $ python manage.py ogrinspect world/data/TM_WORLD_BORDERS/TM_WORLD_BORDERS-0.3.shp WorldBorder


class Source(models.Model):
    name = models.CharField(max_length=255)
    original_url = models.URLField(blank=True, null=True)
    downloaded = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('world:source_detail', kwargs={'pk': self.id})


class Area(models.Model):
    TYPE_CHOICES = (
        ('Country', 'Country'),
        ('ADM1', 'ADM1'),
        ('ADM2', 'ADM2'),
        ('PPLC', 'PPLC'),
        ('PPL', 'PPL')
    )
    political = models.NullBooleanField()
    geographical = models.NullBooleanField()
    historical = models.NullBooleanField()
    name = models.CharField(max_length=255)
    area_type = models.CharField(max_length=255, blank=True, null=True, choices=TYPE_CHOICES)
    source = models.ForeignKey('Source', blank=True, null=True)
    geonames_id = models.IntegerField(blank=True, null=True)
    legacy_properties = HStoreField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_date_written = models.CharField(
        max_length=255, blank=True, null=True,
        validators=[date_validator, ], verbose_name="Start",
        help_text="Please enter a date (DD).(MM).YYYY")
    end_date_written = models.CharField(
        max_length=255, blank=True, null=True,
        validators=[date_validator, ], verbose_name="End",
        help_text="Please enter a date (DD).(MM).YYYY")
    geom = models.MultiPolygonField()
    objects = models.GeoManager()

    def save(self, *args, **kwargs):
        """Adaption of the save() method of the class to automatically parse string-dates into date objects
        """
        def match_date(date):
            """Function to parse string-dates into python date objects.
            """
            date = date.strip()
            date = date.replace('-', '.')
            if re.match(r'[0-9]{4}$', date):
                dr = datetime.strptime(date, '%Y')
                dr2 = date
            elif re.match(r'[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}$', date):
                dr = datetime.strptime(date, '%d.%m.%Y')
                dr2 = date
            elif re.match(r'[0-9]{4}\.\.\.$', date):
                dr = datetime.strptime(date, '%Y...')
                dr2 = re.match(r'([0-9]{4})\.\.\.$', date).group(1)
            elif re.match(r'[0-9]{4}\.[0-9]{1,2}\.\.$', date):
                dr = datetime.strptime(date, '%Y.%m..')
                dr2 = re.match(r'([0-9]{4})\.([0-9]{1,2})\.\.$', date).group(2)
                +'.' + \
                    re.match(r'([0-9]{4})\.([0-9]{1,2})\.\.$', date).group(1)
            elif re.match(r'[0-9]{4}\.[0-9]{1,2}\.[0-9]{1,2}$', date):
                dr = datetime.strptime(date, '%Y.%m.%d')
                dr3 = re.match(
                    r'([0-9]{4})\.([0-9]{1,2})\.([0-9]{1,2})$', date)
                dr2 = dr3.group(3) + '.' + dr3.group(2) + '.' + dr3.group(1)
            else:
                dr = None
                dr2 = dr2 = date
            return dr, dr2
        if self.start_date_written:
            self.start_date, self.start_date_written = match_date(
                self.start_date_written)
        if self.end_date_written:
            self.end_date, self.end_date_written = match_date(
                self.end_date_written)
        super(Area, self).save(*args, **kwargs)
        return self

    @property
    def centroid(self):
        centroid = self.geom.centroid
        coordinates = [centroid.y, centroid.x]
        return coordinates

    @property
    def longitude(self):
        centroid = self.geom.centroid
        return centroid.y

    @property
    def latitude(self):
        centroid = self.geom.centroid
        return centroid.x

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('world:area_detail', kwargs={'pk': self.id})


class Label(models.Model):
    CHOICES_LABELTYPE = (
        ('alternateName', 'alternateName'),
        ('officialName', 'officialName'),
    )

    name = models.CharField(max_length=255, blank=True)
    label_type = models.CharField(
        max_length=255, choices=CHOICES_LABELTYPE, blank=True)
    iso_code = models.CharField(max_length=3, blank=True)
    area = models.ForeignKey(Area, blank=True, null=True)

    def __str__(self):
        return self.name


class AreaArea(models.Model):

    RELATIONTYPE_CHOICES = (
        ('parentCountry', 'parentCountry'),
        ('parentADM1', 'parentADM1'),
        ('parentADM2', 'parentADM2'),
        ('parentADM3', 'parentADM3'),
        ('predecessor', 'predecessor'),
        ('unspecified historical relation', 'unspecified historical relation'),
        ('unspecified geographical relation', 'unspecified geographical relation'),
    )
    RELATIONTYPE_CHOICES_REVERSE = {
        'parentCountry': 'ChildOfCountry',
        'parentADM1': 'childADM1',
        'parentADM2': 'childADM2',
        'parentADM3': 'childADM3',
        'predecessor': 'successor',
        'unspecified historical relation': 'unspecified historical relation',
        'unspecified geographical relation': 'unspecified geographical relation'
    }

    related_areaA = models.ForeignKey(Area, blank=True, null=True, related_name='related_areaA')
    related_areaB = models.ForeignKey(Area, blank=True, null=True, related_name='related_areaB')
    relation_type = models.CharField(max_length=50, choices=RELATIONTYPE_CHOICES, blank=True)
