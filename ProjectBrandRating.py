import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('ProjectData.csv')
rating = df['Avg Rating'].tolist()
fig = ff.create_distplot([rating], ['Mobile Brand Rating'])
fig.show()