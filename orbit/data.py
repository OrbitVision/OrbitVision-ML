selected_sv = ['PG01', 'PE03', 'PR06', 'PC06', 'PC25', 'PJ02']
####### PG01 #######
# G080 2024:352:00000 0000:000:00000 G01
# G080 2024-242A 62339 GPS-IIIA Launched 2024-12-17; NAVSTAR 83

##### PE03 ########
#E212 2016:322:00000 0000:000:00000 E03 
# E212 2016-069B  41860 GAL-2           Launched 2016-11-17; GALILEO 16 (26C)

####### PR06 ########
#R804 2025:358:19350 0000:000:00000 R06 start time from tracking data
# R804 2025-042A  63130 GLO-K2          Launched 2025-03-02; COSMOS 2584

####### PC06 #########
#C220 2026:100:57600 0000:000:00000 C06 [PR04], NABU 20260006
# C220 2019-023A  44204 BDS-3I          Launched 2019-04-20; BEIDOU 3 IGSO-1

####### PC25 ##########
#C212 2018:236:00000 0000:000:00000 C25 
#C212 2018-067B  43603 BDS-3M-SECM-A   Launched 2018-08-24; BEIDOU 3M12

######### PJ02 #########
#J002 2017:152:00000 0000:000:00000 J02 [PR01]
#J002 2017-028A  42738 QZS-2I          Launched 2017-06-01; MICHIBIKI-2


#https://cddis.nasa.gov/archive/gnss/products/2419/
#https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle
#https://files.igs.org/pub/station/general/igs_satellite_metadata.snx
#https://www.space-track.org/#/queryBuilder
#https://www.ngdc.noaa.gov/stp/space-weather/swpc-products/annual_reports/daily_solar_indices_summaries/daily_geomagnetic_data/
#https://www.ngdc.noaa.gov/stp/space-weather/swpc-products/annual_reports/daily_solar_indices_summaries/daily_solar_data/



#*  2026  5 17  9 50  0.00000000
#PG01  14563.180181 -21447.751557  -5580.166732    272.526470
#PE03  -1856.104324 -29104.075914  -5151.187202    -17.565457
#PR06 -15272.190715 -20346.585353  -1722.829286    -19.896249
#PC06 -12914.986320  18833.551511  35507.496732    289.386323
#PC25 -22921.636470  14153.204294  -7253.602690    865.337418
#PJ02 -24857.890879  17576.663091 -24405.961564     -0.191930

import georinex as gr

# file_path = 'orbit_raw/raw_sp3_data/COD0MGXFIN_20261370000_01D_05M_ORB.SP3'

# ds = gr.load(file_path)

# print(ds)

# print("\nLista satelitów w tym pliku:")
# print(ds.sv.values)


import pandas as pd
import json

with open('orbit_raw/raw_sgp4_tle/62339.json', 'r') as f:
    data1 = json.load(f)
df1 = pd.DataFrame(data1)
df1 = df1[['EPOCH', 'TLE_LINE1', 'TLE_LINE2', 'MEAN_MOTION', 'INCLINATION', 'ECCENTRICITY']]
print(df1.loc[0, 'EPOCH'])
print(df1.loc[0, 'TLE_LINE1'])
print(df1.loc[0, 'TLE_LINE2'])
##
with open('orbit_raw/raw_sgp4_tle/41860.json', 'r') as f:
    data2 = json.load(f)
df2 = pd.DataFrame(data2)
df2 = df2[['EPOCH', 'TLE_LINE1', 'TLE_LINE2', 'MEAN_MOTION', 'INCLINATION', 'ECCENTRICITY']]
print(df2.loc[0, 'EPOCH'])
print(df2.loc[0, 'TLE_LINE1'])
print(df2.loc[0, 'TLE_LINE2'])
##
with open('orbit_raw/raw_sgp4_tle/42738.json', 'r') as f:
    data3 = json.load(f)
df3 = pd.DataFrame(data3)
df3 = df3[['EPOCH', 'TLE_LINE1', 'TLE_LINE2', 'MEAN_MOTION', 'INCLINATION', 'ECCENTRICITY']]
print(df3.loc[0, 'EPOCH'])
print(df3.loc[0, 'TLE_LINE1'])
print(df3.loc[0, 'TLE_LINE2'])
##
with open('orbit_raw/raw_sgp4_tle/43603.json', 'r') as f:
    data4 = json.load(f)
df4 = pd.DataFrame(data4)
df4 = df4[['EPOCH', 'TLE_LINE1', 'TLE_LINE2', 'MEAN_MOTION', 'INCLINATION', 'ECCENTRICITY']]
print(df4.loc[0, 'EPOCH'])
print(df4.loc[0, 'TLE_LINE1'])
print(df4.loc[0, 'TLE_LINE2'])
##
with open('orbit_raw/raw_sgp4_tle/44204.json', 'r') as f:
    data5 = json.load(f)
df5 = pd.DataFrame(data5)
df5 = df5[['EPOCH', 'TLE_LINE1', 'TLE_LINE2', 'MEAN_MOTION', 'INCLINATION', 'ECCENTRICITY']]
print(df5.loc[0, 'EPOCH'])
print(df5.loc[0, 'TLE_LINE1'])
print(df5.loc[0, 'TLE_LINE2'])
##
with open('orbit_raw/raw_sgp4_tle/63130.json', 'r') as f:
    data6 = json.load(f)
df6 = pd.DataFrame(data6)
df6 = df6[['EPOCH', 'TLE_LINE1', 'TLE_LINE2', 'MEAN_MOTION', 'INCLINATION', 'ECCENTRICITY']]
print(df6.loc[0, 'EPOCH'])
print(df6.loc[0, 'TLE_LINE1'])
print(df6.loc[0, 'TLE_LINE2'])







from sgp4.api import Satrec, jday
from astropy.coordinates import TEME, ITRS
from astropy import units as u
from astropy.time import Time

sp3_data = {
    '62339': {'l1': "1 62339U 24242A   26136.17689848 -.00000064  00000-0  00000-0 0  9997",
              'l2': "2 62339  54.8632 335.4791 0017144   3.2214 171.9079  2.00570749 10610",
              'pos': [14563.18, -21447.75, -5580.17]},
    '41860': {'l1': "1 41860U 16069B   26134.16349088  .00000049  00000-0  00000-0 0  9999",
              'l2': "2 41860  55.4761 102.0219 0004753 345.7526  14.2010  1.70473991 59075",
              'pos': [-1856.10, -29104.08, -5151.19]},
    '63130': {'l1': "1 63130U 25042A   26135.29222036 -.00000013  00000-0  00000-0 0  9994",
              'l2': "63130  65.0668  73.9199 0006264 234.2965 125.6239  2.13103698  9340",
              'pos': [-15272.19, -20346.59, -1722.83]},
    '44204': {'l1': "1 44204U 19023A   26132.76772565 -.00000227  00000-0  00000-0 0  9990",
              'l2': "2 44204  58.6468  38.0171 0023856 234.3090 349.8662  1.00250503  6851",
              'pos': [-12914.99, 18833.55, 35507.50]},
    '43603': {'l1': "1 43603U 18067B   26134.75259480  .00000100  00000-0  00000-0 0  9995",
              'l2': "2 43603  54.1758 182.1382 0004429  17.6934 342.4159  1.86227418 52523",
              'pos': [-22921.64, 14153.20, -7253.60]},
    '42738': {'l1': "1 42738U 17028A   26135.61781097 -.00000183  00000-0  00000-0 0  9991",
              'l2': "2 42738  39.4779 243.6336 0762341 268.9240  83.1436  1.00292474  7300",
              'pos': [-24857.89, 17576.66, -24405.96]}
}

measurement_time = '2026-05-17 09:50:00'
t = Time(measurement_time, scale='utc')

for norad_id, data in sp3_data.items():
    sat = Satrec.twoline2rv(data['l1'], data['l2'])
    
    jd, fr = jday(t.datetime.year, t.datetime.month, t.datetime.day, 
                  t.datetime.hour, t.datetime.minute, t.datetime.second)
    
    _, pos_teme, _ = sat.sgp4(jd, fr)
    
    teme = TEME(x=pos_teme[0]*u.km, y=pos_teme[1]*u.km, z=pos_teme[2]*u.km, obstime=t)
    itrs = teme.transform_to(ITRS(obstime=t))
    
    print(f"\n--- Satelita {norad_id} ---")
    print(f"SGP4 ECEF: {itrs.x.value:.2f}, {itrs.y.value:.2f}, {itrs.z.value:.2f}")
    print(f"SP3:       {data['pos'][0]:.2f}, {data['pos'][1]:.2f}, {data['pos'][2]:.2f}")