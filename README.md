# django-mikoa

A Django application consisting of all Tanzania locations from Regions to District.

## Prerequisites

* Python 3.6+
* Pip or Pipenv

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
