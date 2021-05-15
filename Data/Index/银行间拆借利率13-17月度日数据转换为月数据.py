import pandas as pd 
data = pd.read_csv("银行间拆借利率13-17月度日数据.csv") 
data.set_index('日期', inplace=True)
data.index = pd.to_datetime(data.index)
print(data.resample('1M').sum())