

import pandas as pd;
import os;
import numpy;
import matplotlib;
import arabic_reshaper
import scipy

from matplotlib import pyplot


read_file = pd.read_excel ("data.xlsx");
read_file.to_csv ("data.csv",
                  index = None,
                  header=True);
data = pd.read_csv("data.csv")
data.info()
data.set_index('Code').plot()
data['Gender']=data['Gender'].astype(str).astype(int)
data.plot(kind='line', x='Joining Year', y='Gender')

#show how many col and rows 
print(data.shape)
data.hist()
pyplot.show()
