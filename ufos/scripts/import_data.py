# scripts/import_data.py
'''
fields:
    0 id,
    1 occurred_at,
    2 city,
    3 state,
    4 country,
    5 shape,
    6 duration_seconds,
    7 duration_text,
    8 description,
    9 reported_on,
    10 latitude,
    11 longitude

like this:
id,occurred_at,city,state,country,shape,duration_seconds,duration_text,description,reported_on,latitude,longitude
1,5/20/2010 21:30,tolland,ct,us,light,10,10 sec,2 red blinking orbs.,6/3/2010,41.8713889,-72.3691667

'''

from datetime import datetime, timedelta
import pytz

from sightings.models import Sighting


def create_sighting(values):

    # try:
    s = Sighting()
    s.sighting_id = int(values[0])

    # Ugh... python hates times in 24:00 format... data contains it.
    if " 24:" in values[1]:
        values[1] = values[1].replace(" 24:"," 23:",1)
        dt = datetime.strptime(values[1], "%m/%d/%Y %H:%M")
        dt = dt + timedelta(hours=1)
    else:
        dt = datetime.strptime(values[1], "%m/%d/%Y %H:%M")

    s.occurred_at = pytz.utc.localize(dt)
    s.city=values[2]
    s.state=values[3]
    s.country=values[4]
    s.shape=values[5]
    s.duration_seconds=float(values[6])
    s.duration_text=values[7].strip()
    s.description=values[8]
    s.reported_on=datetime.strptime(values[9], '%m/%d/%Y').date()
    s.latitude=float(values[10])
    s.longitude=float(values[11])
    # print(f"s is {s.__dict__}")
    # if s.sighting_id == 4:
    #     try:
    #         s.save()
    #     except Exception as e:
    #         import ipdb; ipdb.set_trace()
    # else:
    s.save()

    return True


def run():
    print("importing data from ufo-sightings.csv...")

    i = 0

    with open('../../ufo-sightings.csv') as f:
        for line in f:
            if i == 0:
                i += 1
                continue
            values = list(line.rstrip().split(','))
            if create_sighting(values):
                i += 1
            else:
                return

    print(f"done... processed {i-1} sightings....")