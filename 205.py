import pandas as pd
import numpy as np
import requests
import json
import matplotlib.pyplot as plt
from IPython.display import display



df = pd.DataFrame(requests.get('https://data.cdc.gov/resource/swc5-untb.json').json()),
display(df)
pd.set_option('display.max_columns', None)

df1=df

df1.rename(columns=df.iloc[0]).drop(df.index[0])


