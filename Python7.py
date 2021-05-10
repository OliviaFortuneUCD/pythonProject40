import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

activity = pd.read_csv('Fitbit.csv')

activity1 = activity.copy() # copying the datset to activity1

print(activity1['ActivityDate'].unique())
# adding the yearm month and date columns to the dataset
activity1['year'] = pd.DatetimeIndex(activity1['ActivityDate']).year
activity1['month'] = pd.DatetimeIndex(activity1['ActivityDate']).month
activity1['day'] = pd.DatetimeIndex(activity1['ActivityDate']).day

# facet on the columns with another variable
sns.relplot(y='Calories', x='TotalSteps', hue='TotalDistance', col='month', data = activity1)