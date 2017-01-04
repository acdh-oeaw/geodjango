from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
# automatically genereated by
# $ python manage.py ogrinspect world/data/TM_WORLD_BORDERS/TM_WORLD_BORDERS-0.3.shp WorldBorder


class WorldBorder(models.Model):
    fips = models.CharField(max_length=2)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField()

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
        return reverse('world:world_detail', kwargs={'pk': self.id})


class RegionBorder(models.Model):
    adm1_code = models.CharField(null=True, blank=True, max_length=10)
    objectid_1 = models.IntegerField(null=True, blank=True)
    diss_me = models.IntegerField(null=True, blank=True)
    adm1_cod_1 = models.CharField(null=True, blank=True, max_length=10)
    iso_3166_2 = models.CharField(null=True, blank=True, max_length=10)
    wikipedia = models.CharField(null=True, blank=True, max_length=254)
    iso_a2 = models.CharField(null=True, blank=True, max_length=2)
    adm0_sr = models.IntegerField(null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=100)
    name_alt = models.CharField(null=True, blank=True, max_length=200)
    name_local = models.CharField(null=True, blank=True, max_length=200)
    type = models.CharField(null=True, blank=True, max_length=100)
    type_en = models.CharField(null=True, blank=True, max_length=100)
    code_local = models.CharField(null=True, blank=True, max_length=50)
    code_hasc = models.CharField(null=True, blank=True, max_length=10)
    note = models.CharField(null=True, blank=True, max_length=254)
    hasc_maybe = models.CharField(null=True, blank=True, max_length=50)
    region = models.CharField(null=True, blank=True, max_length=100)
    region_cod = models.CharField(null=True, blank=True, max_length=50)
    provnum_ne = models.IntegerField(null=True, blank=True)
    gadm_level = models.IntegerField(null=True, blank=True)
    check_me = models.IntegerField(null=True, blank=True)
    scalerank = models.IntegerField(null=True, blank=True)
    datarank = models.IntegerField(null=True, blank=True)
    abbrev = models.CharField(null=True, blank=True, max_length=10)
    postal = models.CharField(null=True, blank=True, max_length=10)
    area_sqkm = models.FloatField(null=True, blank=True)
    sameascity = models.IntegerField(null=True, blank=True)
    labelrank = models.IntegerField(null=True, blank=True)
    featurecla = models.CharField(null=True, blank=True, max_length=50)
    name_len = models.IntegerField(null=True, blank=True)
    mapcolor9 = models.IntegerField(null=True, blank=True)
    mapcolor13 = models.IntegerField(null=True, blank=True)
    fips = models.CharField(null=True, blank=True, max_length=5)
    fips_alt = models.CharField(null=True, blank=True, max_length=50)
    woe_id = models.IntegerField(null=True, blank=True)
    woe_label = models.CharField(null=True, blank=True, max_length=250)
    woe_name = models.CharField(null=True, blank=True, max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    sov_a3 = models.CharField(null=True, blank=True, max_length=3)
    adm0_a3 = models.CharField(null=True, blank=True, max_length=3)
    adm0_label = models.IntegerField(null=True, blank=True)
    admin = models.CharField(null=True, blank=True, max_length=200)
    geonunit = models.CharField(null=True, blank=True, max_length=200)
    gu_a3 = models.CharField(null=True, blank=True, max_length=3)
    gn_id = models.IntegerField(null=True, blank=True)
    gn_name = models.CharField(null=True, blank=True, max_length=200)
    gns_id = models.IntegerField(null=True, blank=True)
    gns_name = models.CharField(null=True, blank=True, max_length=200)
    gn_level = models.IntegerField(null=True, blank=True)
    gn_region = models.CharField(null=True, blank=True, max_length=50)
    gn_a1_code = models.CharField(null=True, blank=True, max_length=10)
    region_sub = models.CharField(null=True, blank=True, max_length=250)
    sub_code = models.CharField(null=True, blank=True, max_length=10)
    gns_level = models.IntegerField(null=True, blank=True)
    gns_lang = models.CharField(null=True, blank=True, max_length=10)
    gns_adm1 = models.CharField(null=True, blank=True, max_length=10)
    gns_region = models.CharField(null=True, blank=True, max_length=10)
    geom = models.MultiPolygonField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('world:region_detail', kwargs={'pk': self.id})


# This is an auto-generated Django model module created by ogrinspect.
class AustriaBorders(models.Model):
    kg_nr = models.CharField(max_length=6)
    kg = models.CharField(max_length=50)
    meridian = models.CharField(max_length=3)
    gkz = models.CharField(max_length=6)
    pg = models.CharField(max_length=50)
    bkz = models.CharField(max_length=4)
    pb = models.CharField(max_length=50)
    fa_nr = models.CharField(max_length=3)
    fa = models.CharField(max_length=50)
    gb_kz = models.CharField(max_length=4)
    gb = models.CharField(max_length=50)
    va_nr = models.CharField(max_length=3)
    va = models.CharField(max_length=50)
    bl_kz = models.CharField(max_length=2)
    bl = models.CharField(max_length=50)
    st_kz = models.IntegerField()
    st = models.CharField(max_length=50)
    fl = models.FloatField()
    geom = models.MultiPolygonField()

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
        return self.kg

    def get_absolute_url(self):
        return reverse('world:austria_detail', kwargs={'pk': self.id})
