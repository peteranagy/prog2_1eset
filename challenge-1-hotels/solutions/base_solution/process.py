import pandas as pd
import numpy as np
import json

input_json = json.load(open('input.json','r'))
data_args = json.load(open('data.json','r'))

df = pd.read_csv(data_args['staging_folder'] + '/filtered.csv')

out = []

for place in input_json:
    min_distance = np.inf
    closest_place = {}
    for idx,row in df.iterrows():
        distance = ((place['lon']-row['lon']) ** 2 + (place['lat']-row['lat']) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            closest_place = row[['lon','lat','name']].to_dict()
    out.append(closest_place.copy())


json.dump(out,open('output.json','w'))
