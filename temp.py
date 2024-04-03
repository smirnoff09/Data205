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

print(placesdf.columns.values)
print(walkdf.columns.values)


fips=fips.rename({"County Name":"LocationName", "State":"StateDesc", 'FIPS State':'STATEFP', 'FIPS County':'COUNTYFP'}, axis=1)


placesfips=pd.merge(placesdf, fips, how="outer", on=['LocationName','StateDesc'])
print(placesfips.columns.values)
pd.set_option('display.max_columns', 500)

walkdf=walkdf[['STATEFP','COUNTYFP','CBSA_POP','Ac_Total','Ac_Water','Ac_Land','Ac_Unpr','D1B','D1C','D1C8_RET',
'D1C8_OFF','D1C8_IND','D1C8_SVC','D1C8_ENT','D1C8_ED','D1C8_HLTH','D1C8_PUB', 'NatWalkInd']]

walkdf=walkdf.rename({'CBSA_POP':'pop', 'Ac_Total':'total_area', 'Ac_Water':'water_area', 'Ac_Land':'land_area','Ac_Unpr':'unpr_area','D1B':'pop_density','D1C':'emp_density', 'D1C8_RET':'ret_density','D1C8_OFF':'off_density', 'D1C8_IND':'ind_density','D1C8_SVC':'svc_density','D1C8_ENT':'ent_density','D1C8_ED':'ed_density','D1C8_HLTH':'hlth_density','D1C8_PUB':'pub_density','NatWalkInd':'walk_ind'},axis=1)
print(walkdf.columns.values)


#display(placesfips.dtypes)
placesfips=placesfips.fillna(0)
placesfips = placesfips.astype({'Year':'int64',"STATEFP": 'int64', 'COUNTYFP':'int64'})


#display(walkdf.dtypes)
wpf=pd.merge(placesfips, walkdf, how="outer", on=['STATEFP','COUNTYFP'])

wpf=wpf.fillna(0)
wpf = wpf.astype({'Year':'int64',"STATEFP": 'int64', 'COUNTYFP':'int64'})


wpf.drop(['DataSource', 'Data_Value_Unit', 'Data_Value_Footnote_Symbol', 'Data_Value_Footnote', 'DataValueTypeID', 'Geolocation', 'Counties', "States"], axis=1, inplace=True)
display(wpf.dtypes)
