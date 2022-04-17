import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# データの構造を調査する
filename = 'jissen/project_02/chap_05/data2/eq_data_1_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# マグニチュード、位置データをを取り出す
# 経度（longitude）、経度（latitude）
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# 地震の地図
# data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
    },
}]
my_layout = Layout(title='世界の地震')

fig = {'data': data, 'layout': my_layout}
offline.plot(
    fig,
    filename='jissen/project_02/chap_05/global_earthquakes.html'
)