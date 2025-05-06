#!/usr/bin/env python
"""mapper.py"""

import sys
import numpy as np
import pandas as pd

df = pd.read_csv(sys.stdin,usecols=[0,1,2,3,4,5,6,7,8,9,10])

df.to_csv(sys.stdout)