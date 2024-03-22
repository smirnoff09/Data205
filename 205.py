import pandas as pd
import numpy as np
import requests
import json
import matplotlib.pyplot as plt
from IPython.display import display


#import
df = pd.DataFrame(requests.get('https://data.cdc.gov/resource/swc5-untb.json').json()),
display(df)
pd.set_option('display.max_columns', None)

#desperate attempt at making something work
df1=df

#trying to make first row a header
df1.rename(columns=df.iloc[0]).drop(df.index[0])


