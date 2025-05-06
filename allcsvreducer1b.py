#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import pandas as pd
import numpy as np

df = pd.read_csv(sys.stdin,usecols=[1,2,3,4,5,6,7,8,9,10,11])
df.columns = ['SYMBOL', 'SERIES', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE','TOTTRDQTY', 'TOTTRDVAL', 'TIMESTAMP']

df[['SYMBOL', 'OPEN', 'HIGH', 'LOW','CLOSE']].to_csv(sys.stdout)

