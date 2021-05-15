import plotly
import plotly.offline as pyo
from plotly.graph_objs import *

import pandas as pd

expenseData = pd.read_csv("http://richard-muir.com/data/public/csv/NumberOfMPsExpenseClaims_2010-2015.csv")

traces = []

for i in range(2010,2016):
    x = 'NumberOfClaims' + str(i)
    traces.append({'type' : 'scatter',
                   'mode' : 'lines',
                   'name' : i,
                   'x' : expenseData['month'].tolist(),
                   'y' : expenseData[x].tolist()}
                  )

layout = {'title' : 'Expense claims by month for 2010-2015',
          'xaxis' : {'title' : 'Month'},
          'yaxis' : {'title' : 'Number of expense claims'}
          }

fig = Figure(data=traces, layout=layout)

pyo.plot(fig)