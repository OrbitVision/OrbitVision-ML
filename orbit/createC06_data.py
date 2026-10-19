import pandas as pd

df = pd.read_csv('orbits_2025_processed.csv')

df['sat_id'] = 'P' + df['sat_id']
filtered = df[df['sat_id'] == 'PC06']

filtered.to_csv('PC06_data.csv', index=False)