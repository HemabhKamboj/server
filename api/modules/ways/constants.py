"""
Use Google Maps API to get ways to reach for a given source and destination
Reference:
Place search API: https://developers.google.com/places/web-service/search
Distance Matrix API: https://developers.google.com/maps/documentation/distance-matrix/intro
"""

import os

PLACE_AUTOCOMPLETE_API_BASE_URL = 'https://maps.googleapis.com/maps/api/place/autocomplete/json?input={}&key='
DISTANCE_MATRIX_API_BASE_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&mode={walk_or_drive}&key='
PLACE_SEARCH_API_BASE_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&type={}&key='
# PLACE_AUTOCOMPLETE_API_KEY = os.environ.get('GOOGLE_MAPS_PLACE_AUTOCOMPLETE_API_KEY')
# DISTANCE_MATRIX_API_KEY = os.environ.get('GOOGLE_MAPS_DISTANCE_MATRIX_API_KEY')
PLACE_DETAIL_API_BASIC_URL = 'https://maps.googleapis.com/maps/api/place/details/json?placeid={}&fields=address_component&key='

PLACE_DETAIL_API_KEY = 'AIzaSyCcesKpuRQIMn5QziVLXfstV5d7IYNeqyA'
PLACE_SEARCH_API_KEY = 'AIzaSyCcesKpuRQIMn5QziVLXfstV5d7IYNeqyA'
PLACE_AUTOCOMPLETE_API_KEY = 'AIzaSyCcesKpuRQIMn5QziVLXfstV5d7IYNeqyA'
DISTANCE_MATRIX_API_KEY = 'AIzaSyCcesKpuRQIMn5QziVLXfstV5d7IYNeqyA'
PLACE_AUTOCOMPLETE_API_URL = PLACE_AUTOCOMPLETE_API_BASE_URL + PLACE_AUTOCOMPLETE_API_KEY
PLACE_SEARCH_API_URL = PLACE_SEARCH_API_BASE_URL + PLACE_SEARCH_API_KEY
PLACE_DETAIL_API_URL = PLACE_DETAIL_API_BASIC_URL + PLACE_DETAIL_API_KEY
DISTANCE_MATRIX_API_URL = DISTANCE_MATRIX_API_BASE_URL + DISTANCE_MATRIX_API_KEY
