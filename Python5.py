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
activity1['date'] = pd.DatetimeIndex(activity1['ActivityDate']).day
# figure size
plt.figure(figsize=(15, 8))

# Usual boxplot
ax = sns.boxplot(x='date', y='Calories', data=activity1)

# Add jitter with the swarmplot function.
ax = sns.swarmplot(x='date', y='Calories', data=activity1, color="grey")

ax.set_title('Box plot of Calories with Jitter bu day of the month')