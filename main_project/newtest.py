import numpy as np
import pandas as pd
import tushare as ts
import stockstats
import talib

df = ts.get_hist_data('603863')

stockStat = stockstats.StockDataFrame.retype(df)
close = df.close
highPrice = df.high
lowPrice = df.low
volume = df.volume

df.rename(columns={'close': 'Close', 'volume': 'Volume'}, inplace=True)

sig_k , sig_d  = talib.STOCH(np.array(highPrice), np.array(lowPrice),
							 np.array(close), fastk_period=9,slowk_period=3,
							 slowk_matype=0, slowd_period=3, slowd_matype=0)
sig_j = sig_k * 3 - sig_d  * 2
sig = pd.concat([sig_k, sig_d, sig_j], axis=1, keys=['K', 'D', 'J'])
