from database import firebase
from anomaly import algo
from sensors import sensor
import datetime
import time
import pandas as pd

database = firebase.initialize()
delay = 1 # Setting delay in seconds

while True:
    data = algo.import_df(database)
    timestamp = datetime.datetime.now() # Generating datetime object
    timestamp = int(round(timestamp.timestamp())) # converting datetime object to timestamp
    turbidity = sensor.read_turbidity() # Reading turbidity measurements
    temp = sensor.read_temp() # reading temperature measurements
    #turbidity_anamoly = algo.spcc(data,"turbidity",turbidity) # Checking for turbidity anamoly using spcc
    turbidity_anamoly = algo.ztest(data,"turbidity",turbidity) # Checking for turbidity anamoly using z test
    #temp_anamoly = algo.spcc(data,"temperature",temp) # Checking for temperature anamoly using spcc
    temp_anamoly = algo.ztest(data,"temperature",temp) # Checking for temperature anamoly using z test
    


    # Creating Data Dictionary 
    data = {
        "turbidity":turbidity,
        "temperature":temp,
        "turbidity_anamoly":turbidity_anamoly,
        "temperature_anamoly":temp_anamoly
    }

    firebase.upload(data,timestamp,database) # Upload the data to firebase 
    time.sleep(delay) # Delay 
