import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from database import firebase
from scipy.stats import norm


def spcc(df,feature,value): # Stastical Processes Control Charts
    # Compute the mean and standard deviation of the data
    mean = df[feature].mean()
    std = df[feature].std()

    # Define the control limits for the Shewhart chart
    upper_control_limit = mean + 3*std
    lower_control_limit = mean - 3*std

    if (value > upper_control_limit) or (value < lower_control_limit):
        return True
    else:
        return False


def ztest(df,feature,value):
    alpha = 0.05 # Confidence Interval (0.05 = 95% confidence)
    # Compute the z-score for each data point
    z = (value - df[feature].mean()) / (df[feature].std()/(df[feature].shape[0])**0.5)

    # Defining Critical Points
    z_critical = norm.ppf(1 - (alpha/2))

    # Hypothesis Testing
    if z > z_critical or z < (-1*z_critical): 
        return True
    else:
        return False



def import_df(database):
    f = firebase.read(database) # Read Value from Cloud
    data = pd.DataFrame(dict(f.val())).T
    data.reset_index(level=0, inplace=True)
    data.rename(columns = {'index':'timestamp'}, inplace = True)
    return data 