import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.linearmodels as snsl
import pandas as pd
from datetime import datetime
import tushare as ts
sns.set_style("whitegrid")
end = datetime.today() #开始时间结束时间，选取最近一年的数据
start = datetime(end.year-1,end.month,end.day)
end = str(end)[0:10]
start = str(start)[0:10]

stock = ts.get_hist_data('300104',start,end)#选取一支股票
stock['close'].plot(legend=True ,figsize=(10,4))#股票收盘价走势曲线
#plt.show()

stock[['close','ma5','ma10','ma20']].plot(legend=True ,figsize=(10,4))#做出5日均线、10日均线以及20日均线
# plt.show()#
stock['Daily Return'] = stock['close'].pct_change()
stock['Daily Return'].plot(legend=True,figsize=(10,4))
plt.show()

# sns.jointplot(stock['Daily Return'],stock['Daily Return'],alpha=0.2)
# stock_lis=['300113','300343','300295','300315']#随便选取了四支互联网相关的股票
# df=pd.DataFrame()
# for stock in stock_lis:
#      closing_df = ts.get_hist_data(stock,start,end)['close']
#      df = df.join(pd.DataFrame({stock:closing_df}),how='outer')
# tech_rets = df.pct_change()
# snsl.corrplot(tech_rets.dropna())
# plt.show()

