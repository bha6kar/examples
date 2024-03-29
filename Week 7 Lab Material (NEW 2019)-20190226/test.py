import requests
from pprint import pprint

crime_url_template = 'https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={date}'
categories_url_template = 'https://data.police.uk/api/crime-categories?date={date}'

my_latitude = '51.52369'
my_longitude = '-0.0395857'
my_date = '2018-11'

crime_url = crime_url_template.format(
    lat=my_latitude, lng=my_longitude, date=my_date)

respons = requests.get(crime_url)

if respons.ok:
    crimes = respons.json()
else:
    print(respons.reason)

# pprint(crimes)


resp = requests.get(categories_url_template.format(date=my_date))
if resp.ok:
    categories_json = resp.json()
else:
    print(resp.reasone)

categories = {categ["url"]: categ["name"] for categ in categories_json}
crime_category_stats = dict.fromkeys(categories.keys(), 0)
crime_category_stats.pop("all-crime")

for crime in crimes:
    crime_category_stats[crime["category"]] += 1
# pprint(crime_category_stats)

crime_outcome_stats = {'None': 0}

pprint(crime_outcome_stats)

for crime in crimes:
    outcome = crime["outcome_status"]
    if not outcome:
        crime_outcome_stats['None'] += 1
    elif outcome['category'] not in crime_outcome_stats.keys():
        crime_outcome_stats.update({outcome['category']: 1})
    else:
        crime_outcome_stats[outcome['category']] += 1

print(crime_outcome_stats)
