import tushare as ts
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ochl
import numpy as np
import pandas as pd
from matplotlib.pylab import date2num
import matplotlib.ticker as ticker
import time
pro = ts.pro_api("cec49f05bf7d7177704aa020140bcb9aa7656181118f3748806f5bdc")
data=pro.daily(ts_code='601088.SH',start_date='20200922', end_date='20210110')
data=data[['trade_date','open','close','high','low','vol']]
data[data['vol']==0]=np.nan
data=data.dropna()
data.sort_values(by='trade_date',ascending=True,inplace=True)
data[-5:]
