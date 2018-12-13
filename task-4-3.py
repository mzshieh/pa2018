import requests
import json

res = requests.get('http://opendata.epa.gov.tw/ws/Data/UV/?$format=json')
data = json.loads(res.text)

cand = []
for site in data:
    name = site.get('SiteName')
    uvi = site.get('UVI')
    if name == None or uvi == None:
        continue
    cand.append((name,uvi))
    
cand.sort(key=lambda x: -float(x[1]))
for site in cand[:3]:
    print(*site)












