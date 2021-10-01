# django-mikoa

A Django application consisting of all Tanzania locations from Regions to District. The full tutorial on how to integrate on django project found on [How to create dependent dropdown list of Tanzania Region by Django Ajax](https://sogea.co.tz/150003-how-to-create-dependent-dropdown-list-of-tanzania-region-by-django-ajax/)

## Prerequisites

* Python 3.6+
* Pip or Pipenv

## It will Cover

* [x] Regions (region, capital, number of districts, area, population, postcode and zone)
* [x] Districts (district, region, population)
* [ ] Wards
* [ ] Vilage/Streets

## Installation

This package is available in [Python Package Index](https://pypi.org/project/django-mikoa/) and can be installed using `pip` or `pipenv`

1. Run ``pip install django-mikoa``
2. Add ``mikoa`` to ``INSTALLED_APPS``
3. Run ``python manage.py migrate``

## Usage

### To access Tanzania Regions

```python
from mikoa.models import Region
regions = Region.objects.all()

print(regions)
```

### To access Tanzania Districts

```python
from mikoa.models import District
districts = District.objects.all()

print(districts)
```

### To access all Districts of Certain Region

```python
from mikoa.models import Region, District
regions = Region.objects.all()

for region in regions:
    for district in region.district_set.all():
        print(district.region.name)
        print(district.name)   
```

## Give it a star

If you found this repository useful, give it a star so as the whole galaxy of developer can get to know it.

## Bug bounty?

If you encounter issue with the usage of the package, feel free raise an issue so as we can fix it as soon as possible(ASAP).

## Pull Requests

If you have something to add I welcome pull requests on improvement , you're helpful contribution will be merged as soon as possible

## Disclaimer

All the location I used to build this repository, I got from an public repository titled [tanzania-locations-db](https://github.com/HackEAC/tanzania-locations-db), I'm not responsible for any kind of misinformation in it, So use it to your own risk
