import pandas as pd
import json

args = json.load(open('data.json','r'))

df = pd.read_csv(args['datafile'])

df[['lon','lat','name']].to_feather(args['staging_folder'] + '/filtered.feather')
