# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 10:23:01 2015

@author: Amanda
"""

import pandas as pd
from ggplot import *

url = 'http://ghdx.healthdata.org/sites/default/files/'\
      'record-attached-files/IHME_PHMRC_VA_DATA_ADULT_Y2013M09D11_0.csv'
      
#df = pd.read_csv(url)

df = pd.read_csv(url, low_memory=False)

df.head()