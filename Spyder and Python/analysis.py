# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 09:00:53 2023

@author: RSKamath
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns

data = pd.read_parquet("parsed_data_public.parquet")