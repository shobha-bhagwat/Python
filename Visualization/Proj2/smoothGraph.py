from pandas_datareader import data
from scipy import signal

import plotly
import plotly.offline as pyo
from plotly.graph_objs import *
import plotly.plotly as py

import pandas as pd

plotly.tools.set_credentials_file(username='&&&&&   ', api_key='*******')

appleVals = data.get_data_yahoo('AAPL','1/1/2012','1/1/2013')  ##Apple stock price for 1 year

unSmooth = {'type' : 'scatter',
            'mode' : 'lines',
            'name' : 'Apple (unSmooth)',
            'x' : appleVals.index,
            'y' : appleVals['Close'],
            'line' : {'smoothing' : 0,
                      'shape' : 'spline',
                      'width' : 1}
            }

smooth = {'type' : 'scatter',
            'mode' : 'lines',
            'name' : 'Apple (smooth)',
            'x' : appleVals.index,
            'y' : appleVals['Close'] + 50,
            'line' : {'smoothing' : 1.3,
                      'shape' : 'spline',
                      'width' : 2}
            }

layout = {'title' : 'Apple Stock closing price for year 2012',
          'xaxis' : {'title' : 'Date'},
          'yaxis' : {'title' : 'Closing price ($)'}
          }

newSmooth = {'type' : 'scatter',
            'mode' : 'lines',
            'name' : 'Apple (newSmooth)',
            'x' : appleVals.index,
            'y' : signal.savgol_filter(appleVals['Close'], 51, 3),
            'line' : {'smoothing' : 1.3,
                      'shape' : 'spline',
                      'width' : 2.5}
            }



fig = Figure(data=[unSmooth,smooth,newSmooth], layout=layout)

pyo.plot(fig)

py.plot(fig, filename = 'Apple Stock Price')