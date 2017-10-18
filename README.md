## Summary

quick Django interview question -- four API endpoints to answer questions about a UFO invasion.
  
Typically I would use something lighterweight
thank Django or Rails for serving up APIs (either Flask or Sinatra, etc.) but I've been working
on Django stuff recently and this was a quick way to do it.


I would definitely/typically NOT submit a PR without tests, but... time. Ideally it is
TDD (breaking tests first, implement feature,make them pass.... the usual goodness).

## Requirements

You'll need python 3.6 and pip (Python package manager) locally to run this solution.  Typically I install this in a python `virtuanlenv` to isolate
any libraries/dependencies -- see 

`https://virtualenvwrapper.readthedocs.io/en/latest/` 

or  

`http://docs.python-guide.org/en/latest/dev/virtualenvs/`

for info on how to create a virtual env for python apps.  To verify that you have a Python 3.6 environment
before continuing, run

```
python -V
```

and you should see something like

```
Python 3.6.2
```

Once you download this project from GitHub, navigate to the directory where you downloaded it, and
with Python 3.6 as the current python, do the following steps:

1. cd `solution/ufos` so that you're in same directory as `manage.py` command
2. run `pip install -r requirements.txt` to install all app required python libs
3. run `python manage.py migrate` to create database and model
4. run `python manage.py runscript import_data` to import data from csv file
 

## Usage

In the `solutions/ufos` folder, run `python manage.py runserver` to run the django API server locally. 
From there you can hit the API endpoints using the browser or `curl` or whatever you like:

http://localhost:8000/sightings  (Question #0)
http://localhost:8000/fleet (Question #1)
http://localhost:8000/evacuation (Question #2)
http://localhost:8000/attacks  (Question #3)

## Answers

# Question #0 - How Many UFO Sightings?

To make sure you're up to the task, NASA is starting you off with a simple one.
How many UFO sightings across the entire globe do we have in our dataset?

NASA kindly has provided the answer to this one just to make sure you've loaded the dataset correctly.
Write an endpoint to serve up this counter and confirm that you and NASA are on the same page with a count of `80332` sightings.

The HTTP service for this question should work in the following way:

```bash
⇒  curl http://localhost:<port>/<route>?<optional-query-string>
{
  "count": 80332
}
```
Answer:
```
time curl http://localhost:8000/sightings
{"count": 80332}

curl http://localhost:8000/sightings  0.00s user 0.01s system 62% cpu 0.016 total
```

# Question #1: How Advanced is the Fleet?

NASA and defense forces are scrambling to determine the capabilities of the Alien fleet, more specifically, how many different types of spaceships do they have?
As a simple approximation, just calculate the number of unique shapes of alien ships that have been seen across the globe.

If a UFO sighting does not describe a shape of the UFO, it can be ignored for this calculation.

The HTTP service for this question should work in the following way:

```bash
⇒  curl http://localhost:<port>/<route>?<optional-query-string>
{
  "count": <unique_ship_shape_count:int>
}
```

## Answer:
```
time curl http://localhost:8000/fleet
{"count": 30}

curl http://localhost:8000/fleet  0.00s user 0.00s system 29% cpu 0.029 total
```

# Question #2: Evacuation Priorities

With limited resources, the National Guard is looking to prioritize evacuation efforts based on cities that are likely to be attacked first.
With the assumption that cities will be attacked based on the number of previous UFO sightings,
find the Top-10 Cities in the United States with the most UFO sightings.

Cities should be returned in descending order from most sightings to least.

The HTTP service for this question should work in the following way:

```bash
⇒  curl http://localhost:<port>/<route>?<query-string>
{
  "sightings": [
    {
        "city": <city_name_with_most_sightings:string>,
        "count": <sightings_in_this_city:int>
    },
    {
        "city": <city_name_with_second_most_sightings:string>,
        "count": <sightings_in_this_city:int>
    },
    ...
    ...
    {
        "city": <city_name_with_tenth_most_sightings:string>,
        "count": <sightings_in_this_city:int>
    }
  ]
}
```
## Answer:
```
time curl http://localhost:8000/evacuation
{"sightings": [{"city": "seattle", "count": 525}, {"city": "phoenix", "count": 454}, {"city": "portland", "count": 374}, {"city": "las vegas", "count": 368}, {"city": "los angeles", "count": 353}, {"city": "san diego", "count": 338}, {"city": "houston", "count": 297}, {"city": "chicago", "count": 265}, {"city": "tucson", "count": 241}, {"city": "miami", "count": 239}]}

curl http://localhost:8000/evacuation  0.00s user 0.00s system 2% cpu 0.297 total
```

# Question #3: One if by Land

Prior to the invasion fleet arriving, the government rounded up high ranking scientists, engineers, and software developers
and took them to a secret underground base, codename: **Area 52**. The location of Area 52 is highly classified and not even you know its exact location.

You thought you were safe. However, rumors are afloat and everyone speaks in hushed whispers.
It seems that the Aliens may have figured out the hidden location of Area 52. Now you're being tasked with an impossible request:
Figure out where the Alien attack will come from.

Lucky for you, someone scrawled the GPS coordinates of Area 52 on the inside of a bathroom stall. Go figure.

Location: `46.5476, -87.3956`

Given these GPS coordinates, find the three geographically closest UFO sightings where an attack would originate from.

Sightings should be returned in descending order by distance, from closest to furthest away.
Each sighting returned should contain all fields available.

You do not need to consider that the Earth is an ellipsoid/spheroid. For the purposes of this computation, it is
safe to assume that it is a perfect sphere and that will accurate enough.

The HTTP service for this question should work in the following way:

```bash
⇒  curl http://localhost:<port>/<route>?<query-string>
{
  "sightings": [
    {
        "city": <city_closest_to_base:string>,
        "country": <country_of_city:string>,
        ...
        ...
        "shape": <shape_of_ufo:string>
    },
    {
        "city": <city_second_closest:string>,
        "country": <country_of_city:string>,
        ...
        ...
        "shape": <shape_of_ufo:string>
    },
    {
        "city": <city_third_closest:string>,
        "country": <country_of_city:string>,
        ...
        ...
        "shape": <shape_of_ufo:string>
    }
  ]
}
```
## Answer:
```
time curl http://localhost:8000/attacks/\?reference_point\=\(46.5476,-87.3956\)\&num_closest\=3
{"sightings": [{"city": "marquette", "country": "us", "state": "mi", "occurred_at": "1974-06-01T00:00:00Z", "duration_seconds": 300.0, "duration_text": "5 minutes", "description": "We had no idea what it was and did not speak of it for years.", "reported_on": "2006-02-14", "latitude": "46.5436111", "longitude": "-87.3952778", "shape": "oval"}, {"city": "upper peninsula", "country": "", "state": "mi", "occurred_at": "2011-10-27T21:00:00Z", "duration_seconds": 300.0, "duration_text": "5 minutes", "description": "Two brilliant red lights&#44 side-by-side&#44 moved together&#44 then apart continuing west.", "reported_on": "2011-12-12", "latitude": "46.5374760", "longitude": "-87.3952110", "shape": "light"}, {"city": "harvey", "country": "us", "state": "mi", "occurred_at": "1988-08-18T14:45:00Z", "duration_seconds": 180.0, "duration_text": "3 minutes", "description": "Very large dual disk saucer &#44counter rotating hovering and finally submerging into lake superior about 1/2 mile offshore.", "reported_on": "2012-10-30", "latitude": "46.4947222", "longitude": "-87.3541667", "shape": "other"}]}

curl   0.00s user 0.00s system 21% cpu 0.039 total
```


