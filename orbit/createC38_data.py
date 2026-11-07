import pandas as pd

df = pd.read_csv('big_data/orbits_2024_processed.csv')

df['sat_id'] = 'P' + df['sat_id']
filtered = df[df['sat_id'] == 'PC38']

filtered.to_csv('PC38_data_2024_sp3.csv', index=False)