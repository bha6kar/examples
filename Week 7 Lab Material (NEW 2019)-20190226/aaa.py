import requests
from pprint import pprint
crime_url_template = 'https://data.police.uk/api/outcomes-for-crime/{id}'
crime_id = '590d68b69228a9ff95b675bb4af591b38de561aa03129dc09a03ef34f537588c'

crime_url = crime_url_template.format(id=crime_id)
resp = requests.get(crime_url)
if resp.ok:
    crimes = resp.json()
else:
    print(resp.reason)
pprint(crimes)
