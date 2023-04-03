from database import firebase
from anomaly import algo
from sensors import sensor
import datetime
import time
import pandas as pd

database = firebase.initialize()
data = algo.import_df(database)
turbidity = 10000
temperature = 100
turbidity_anamoly = algo.ztest(data,"turbidity",turbidity) # Checking for turbidity anamoly
temp_anamoly = algo.ztest(data,"temperature",temperature) # Checking for temperature anamoly

timestamp = datetime.datetime.now() # Generating datetime object
timestamp = int(round(timestamp.timestamp())) # converting datetime object to timestamp
data = {
    "turbidity":turbidity,
    "temperature":temperature,
    "turbidity_anamoly":turbidity_anamoly,
    "temperature_anamoly":temp_anamoly
}
firebase.upload(data,timestamp,database) # Upload the data to firebase 