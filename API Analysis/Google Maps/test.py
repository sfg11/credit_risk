import googlemaps
Key ='AIzaSyCbE5u5-3CmLSKbMl-BOME5SSsrwzEvGFg'
gmaps = googlemaps.Client(key=Key)
details = gmaps.places_autocomplete_query('Fortinos near Oakville, ON, Canada')[0]['description']
print(details)