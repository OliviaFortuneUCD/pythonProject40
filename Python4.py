import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

activity = pd.read_csv('Fitbit.csv')

sns.lmplot(x='TotalSteps', y='Calories', data=activity)