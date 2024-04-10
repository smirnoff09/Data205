import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
%pip install seaborn
import seaborn as sns


places = pd.read_csv('PLACES.csv')
dentist=pd.read_csv('DENTIST.csv')
fips=pd.read_csv('FIPS.csv')
placesdf=pd.DataFrame(places)

fips=fips.rename({"County Name":"LocationName", "State":"StateDesc", 'FIPS State':'STATEFP', 'FIPS County':'COUNTYFP'}, axis=1)

placesfips=pd.merge(placesdf, fips, how="outer", on=['LocationName','StateDesc'])

pd.set_option('display.max_columns', 40)

placesfips=placesfips.fillna(0)
placesfips = placesfips.astype({'Year':'int64',"STATEFP": 'int64', 'COUNTYFP':'int64'})
placesfips["STATEFP"] = placesfips["STATEFP"].astype("string").str.zfill(2)
placesfips["COUNTYFP"] = placesfips["COUNTYFP"].astype("string").str.zfill(3)
placesfips['FULLFIPS'] = placesfips['STATEFP'].astype(str) + placesfips['COUNTYFP']

placesfips.drop(['Year','StateAbbr','Category','DataSource','Data_Value_Footnote_Symbol','Data_Value_Footnote','LocationID','DataValueTypeID','Geolocation','CategoryID','Counties','States','STATEFP','COUNTYFP'], axis=1, inplace=True)
placesfips.head()

dentist=dentist.rename({"cnty_name":"LocationName", "st_name":"StateDesc", 'fips_st':'STATEFP', 'fips_cnty':'COUNTYFP'}, axis=1)
dentist["STATEFP"] = dentist["STATEFP"].astype("string").str.zfill(2)
dentist["COUNTYFP"] = dentist["COUNTYFP"].astype("string").str.zfill(3)
dentist['FULLFIPS'] = dentist['STATEFP'].astype(str) + dentist['COUNTYFP']

dentpl=pd.merge(placesfips, dentist, how="outer", on=['FULLFIPS'])
dentpl.head()


dentpl_age = dentpl.drop(dentpl[dentpl['Data_Value_Type'] == 'Crude prevalence'].index)
dentpl_crude = dentpl.drop(dentpl[dentpl['Data_Value_Type'] == 'Age-adjusted prevalence'].index)

