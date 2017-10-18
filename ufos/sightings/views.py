import ast
from operator import itemgetter

from geopy import distance

from django.db.models import Count
from django.http import JsonResponse, HttpResponse

from sightings.models import Sighting


def index(request):
    return HttpResponse("Hello, You're at the UFO Sightings Index!")


def sightings(request):
    ''' Question 0'''
    num_sightings = Sighting.objects.count()
    return JsonResponse({"count": num_sightings})


def fleet(request):
    ''' Question 1'''
    shapes = Sighting.objects.values('shape').annotate(count=Count('shape'))
    types_of_spaceships = len(shapes)
    return JsonResponse({"count": types_of_spaceships})


def evacuation(request):
    ''' Question 2'''
    sightings_by_city = Sighting.objects.all().order_by('city').values('city').annotate(count=Count('sighting_id'))
    sorted_sightings = sorted(sightings_by_city, key=itemgetter('count'), reverse=True)
    top_ten = sorted_sightings[:10]
    return JsonResponse({"sightings": top_ten}, safe=False)


def attacks(request):
    ''' Question 3'''

    # ast.literal_eval is safe: https://goo.gl/gBn7Xt
    reference_point = ast.literal_eval(request.GET.get('reference_point'))
    num_closest = int(request.GET.get('num_closest'))

    invalid_lat = reference_point[0] > 90 or reference_point[0] < -90
    invalid_lng = reference_point[1] > 180 or reference_point[1] < -180
    if invalid_lat or invalid_lng:
        raise ValueError("Error: Invalid Lat/Long value specified")

    distances = []
    min_lat = reference_point[0] - 1
    max_lat = reference_point[0] + 1
    min_lng = reference_point[1] - 1
    max_lng = reference_point[1] + 1

    while len(distances) < num_closest:
        nearby_sightings = Sighting.objects.filter(latitude__gt=min_lat, latitude__lt=max_lat, longitude__gt=min_lng,
                                            longitude__lt=max_lng)
        if len(nearby_sightings) > 0:
            sighting_distances = [(idx,
                                   distance.vincenty(reference_point, (s.latitude, s.longitude)).miles,
                                   s.latitude,
                                   s.longitude,
                                   s.pk) for idx, s
                                  in enumerate(nearby_sightings)]

            sorted_distances = sorted(sighting_distances, key=lambda s: s[1])
            for s in sorted_distances:
                # we skip over lats/longs that we've already included, because we're returning
                # num_closest locations.  If a location (as defined by coordinates) has already been seen, find the next
                # nearest one.
                if len([d for d in distances if d[2] == s[2] and d[3] == s[3]]) == 0:
                    distances.append(s)
                    if len(distances) == num_closest:
                        break

            if min_lat > -90: min_lat -= 1
            if max_lat < 90: min_lat += 1
            if min_lng > -180: min_lng -= 1
            if max_lng < 180: max_lng += 1


    keys = [d[4] for d in distances]

    closest_sightings = []
    for k in keys:

        s = Sighting.objects.values(
            'city',
            'country',
            'state',
            'occurred_at',
            'duration_seconds',
            'duration_text',
            'description',
            'reported_on',
            'latitude',
            'longitude',
            'shape'
        ).get(id=k)
        closest_sightings.append(s)

    return JsonResponse({"sightings": closest_sightings}, safe=False)



