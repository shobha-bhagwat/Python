import pandas as pd
import matplotlib.pyplot as plt

inputfile = "C:/Users/shbhagwa/Downloads/data/ecomdata.csv"

df = pd.read_csv("C:/Users/shbhagwa/Downloads/data/ecomdata.csv", encoding='latin1')

###### Highest selling product in each country #####

df1 = df.loc[:, ['StockCode', 'Quantity', 'Country']]  ##which product is sold maximum in which country

df1 = df1.groupby(['Country', 'StockCode']).Quantity.agg({'Quantity': sum})

df11 = df1.loc[df1.groupby(['Country'])['Quantity'].idxmax()]

print(df11)

########### Sales-by-Country graph

df2 = df.loc[:, ['Country', 'Quantity']]  ## monthly trending

df2 = df2.groupby(['Country']).Quantity.agg({'Quantity': sum})

bar_plot = df2.plot(kind='bar',legend=None,title="Total Sales by Country")
bar_plot.set_xlabel("Country")
bar_plot.set_ylabel("Quantity")
plt.show()

##### Customer per country who did highest purchase

df3 = df.loc[:, ['Quantity', 'UnitPrice', 'CustomerID', 'Country']]

df3['Purchase'] = df3['UnitPrice'] * df3['Quantity']

df3['Purchase'] = df3['Purchase'].astype(int)

df3 = df3.groupby(['Country', 'CustomerID']).Purchase.agg({'Purchase': sum})

df33 = df3.loc[df3.groupby(['Country'])['Purchase'].idxmax()]

print(df33)

###### Most frequent customer per country

df4 = df.loc[:, ['Country', 'CustomerID', 'InvoiceDate']]

df4['InvoiceDate'] = pd.to_datetime(df4['InvoiceDate'])

df4['InvoiceDate_DT'] = df4['InvoiceDate'].dt.date

df4 = df4.groupby(['Country', 'CustomerID', 'InvoiceDate_DT']).size().reset_index(name='counts')

df4 = df4.loc[:, ['Country', 'CustomerID', 'InvoiceDate_DT']]

df4 = df4.groupby(['Country', 'CustomerID']).size().reset_index(name='maxcount')

df44 = df4.loc[df4.groupby(['Country'])['maxcount'].idxmax()]

print(df44)