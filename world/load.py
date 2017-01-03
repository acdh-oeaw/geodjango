import os
from django.contrib.gis.utils import LayerMapping
from .models import RegionBorder, WorldBorder, AustriaBorders

worlboarder_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'geom': 'MULTIPOLYGON',
}

regionborder_mapping = {
    'adm1_code': 'adm1_code',
    'objectid_1': 'OBJECTID_1',
    'diss_me': 'diss_me',
    'adm1_cod_1': 'adm1_cod_1',
    'iso_3166_2': 'iso_3166_2',
    'wikipedia': 'wikipedia',
    'iso_a2': 'iso_a2',
    'adm0_sr': 'adm0_sr',
    'name': 'name',
    'name_alt': 'name_alt',
    'name_local': 'name_local',
    'type': 'type',
    'type_en': 'type_en',
    'code_local': 'code_local',
    'code_hasc': 'code_hasc',
    'note': 'note',
    'hasc_maybe': 'hasc_maybe',
    'region': 'region',
    'region_cod': 'region_cod',
    'provnum_ne': 'provnum_ne',
    'gadm_level': 'gadm_level',
    'check_me': 'check_me',
    'scalerank': 'scalerank',
    'datarank': 'datarank',
    'abbrev': 'abbrev',
    'postal': 'postal',
    'area_sqkm': 'area_sqkm',
    'sameascity': 'sameascity',
    'labelrank': 'labelrank',
    'featurecla': 'featurecla',
    'name_len': 'name_len',
    'mapcolor9': 'mapcolor9',
    'mapcolor13': 'mapcolor13',
    'fips': 'fips',
    'fips_alt': 'fips_alt',
    'woe_id': 'woe_id',
    'woe_label': 'woe_label',
    'woe_name': 'woe_name',
    'latitude': 'latitude',
    'longitude': 'longitude',
    'sov_a3': 'sov_a3',
    'adm0_a3': 'adm0_a3',
    'adm0_label': 'adm0_label',
    'admin': 'admin',
    'geonunit': 'geonunit',
    'gu_a3': 'gu_a3',
    'gn_id': 'gn_id',
    'gn_name': 'gn_name',
    'gns_id': 'gns_id',
    'gns_name': 'gns_name',
    'gn_level': 'gn_level',
    'gn_region': 'gn_region',
    'gn_a1_code': 'gn_a1_code',
    'region_sub': 'region_sub',
    'sub_code': 'sub_code',
    'gns_level': 'gns_level',
    'gns_lang': 'gns_lang',
    'gns_adm1': 'gns_adm1',
    'gns_region': 'gns_region',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for Austria model
austria_mapping = {
    'kg_nr': 'KG_NR',
    'kg': 'KG',
    'meridian': 'MERIDIAN',
    'gkz': 'GKZ',
    'pg': 'PG',
    'bkz': 'BKZ',
    'pb': 'PB',
    'fa_nr': 'FA_NR',
    'fa': 'FA',
    'gb_kz': 'GB_KZ',
    'gb': 'GB',
    'va_nr': 'VA_NR',
    'va': 'VA',
    'bl_kz': 'BL_KZ',
    'bl': 'BL',
    'st_kz': 'ST_KZ',
    'st': 'ST',
    'fl': 'FL',
    'geom': 'MULTIPOLYGON',
}

austria_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        'data', 'VGD-Oesterreich_gen_250', 'BEV_VGD_250_LAM_mitAttributen_shp_2016_10_02.shp'),
)

region_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        'data', 'ne_10m_admin_1_states_provinces', 'ne_10m_admin_1_states_provinces.shp'),
)

world_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        'data', 'TM_WORLD_BORDERS-0.3', 'TM_WORLD_BORDERS-0.3.shp'),
)


def import_austria(verbose=True):
    lm = LayerMapping(
        AustriaBorders, austria_shp, austria_mapping,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)


def import_regions(verbose=True):
    lm = LayerMapping(
        RegionBorder, region_shp, regionborder_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)


def import_countries(verbose=True):
    lm = LayerMapping(
        WorldBorder, world_shp, worlboarder_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
