import pandas as pd  
import pandas_datareader.data as web  
import datetime  
  
start = datetime.datetime(2010,1,1)  
end = datetime.date.today()  
apple = web.DataReader("AAPL", "yahoo", start, end)  
print(apple.head())  

##### save data  
apple.to_csv(path_or_buf='data_AAPL.csv')  
  
##### read the data from .csv when need  
apple=pd.read_csv(filepath_or_buffer='data_AAPL.csv')  
print(apple.head())  