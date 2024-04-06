import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
import csv


places = pd.read_csv('PLACES.csv')

walk=pd.read_csv('WALKABILITY.csv')

fips=pd.read_csv('FIPS.csv')


placesdf=pd.DataFrame(places)

walkdf=pd.DataFrame(walk)

display(placesdf.dtypes)
display(walkdf.dtypes)
display(fips.dtypes)

fips=fips.rename({"County Name":"LocationName", "State":"StateDesc", 'FIPS State':'STATEFP', 'FIPS County':'COUNTYFP'}, axis=1)
print(fips.head)

placesfips=pd.merge(placesdf, fips, how="outer", on=['LocationName','StateDesc'])
display(placesfips.dtypes)
pd.set_option('display.max_columns', 500)

walkdf=walkdf[['STATEFP','COUNTYFP','CBSA_POP','Ac_Total','Ac_Water','Ac_Land','Ac_Unpr','D1B','D1C','D1C8_RET',
'D1C8_OFF','D1C8_IND','D1C8_SVC','D1C8_ENT','D1C8_ED','D1C8_HLTH','D1C8_PUB', 'NatWalkInd']]

walkdf=walkdf.rename({'CBSA_POP':'pop', 'Ac_Total':'total_area', 'Ac_Water':'water_area', 'Ac_Land':'land_area','Ac_Unpr':'unpr_area','D1B':'pop_density','D1C':'emp_density', 'D1C8_RET':'ret_density','D1C8_OFF':'off_density', 'D1C8_IND':'ind_density','D1C8_SVC':'svc_density','D1C8_ENT':'ent_density','D1C8_ED':'ed_density','D1C8_HLTH':'hlth_density','D1C8_PUB':'pub_density','NatWalkInd':'walk_ind'},axis=1)
display(walkdf.dtypes)

walkfips=pd.merge(walkdf, fips, how="outer", on=['STATEFP','COUNTYFP'])
display(walkfips.dtypes)

placesfips=placesfips.fillna(0)
placesfips = placesfips.astype({'Year':'int64',"STATEFP": 'int64', 'COUNTYFP':'int64'})

walkfips=walkfips.fillna(0)

placesfips["STATEFP"] = placesfips["STATEFP"].astype("string").str.zfill(2)
placesfips["COUNTYFP"] = placesfips["COUNTYFP"].astype("string").str.zfill(3)

walkfips["STATEFP"] = placesfips["STATEFP"].astype("string").str.zfill(2)
walkfips["COUNTYFP"] = placesfips["COUNTYFP"].astype("string").str.zfill(3)

placesfips['FULLFIPS'] = placesfips['STATEFP'].astype(str) + placesfips['COUNTYFP']

walkfips['FULLFIPS'] = walkfips['STATEFP'].astype(str) + walkfips['COUNTYFP']

walkfips_agg=walkfips.groupby('FULLFIPS').agg({'pop':'mean','total_area':'sum','water_area':'sum','land_area':'sum',
'unpr_area':'sum','pop_density':'mean','emp_density':'mean','ret_density':'mean',
'off_density':'mean','ind_density':'mean','svc_density':'mean','ent_density':'mean',
'ed_density':'mean','hlth_density':'mean','pub_density':'mean','walk_ind':'mean'})

wpf=pd.merge(placesfips, walkfips_agg, how="outer", on=['FULLFIPS'])

wpf.drop(['DataSource', 'Data_Value_Unit', 'Data_Value_Footnote_Symbol', 'Data_Value_Footnote', 'DataValueTypeID', 'Geolocation', 'Counties', "States"], axis=1, inplace=True)

wpf1=wpf.dropna()
