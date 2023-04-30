#covid19api.com

from sre_compile import MAXCODE
import requests

response = requests.get('https://api.covid19api.com/summary')
rjson = response.json()

cl = len(rjson['Countries'])
maxc = 0

for i in range(cl):
    cases = rjson['Countries'][i]['TotalConfirmed']
    country = rjson['Countries'][i]['Country']

    if cases > maxc:
        maxc = cases
        maxco = country


print(maxco)
