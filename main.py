from database import firebase
from anamoly import algo
from sensors import sensor
import datetime
import time
import pandas as pd

database = firebase.initialize()
delay = 1 # Setting delay in seconds

n = 0
while n<20:
    try:
        data = algo.import_df(database)
        timestamp = datetime.datetime.now() # Generating datetime object
        timestamp = int(round(timestamp.timestamp())) # converting datetime object to timestamp
        turbidity = sensor.read_turbidity() # Reading turbidity measurements
        temp = sensor.read_temp() # reading temperature measurements
        turbidity_anamoly = algo.spcc(data,"turbidity",turbidity) # Checking for turbidity anamoly
        #turbidity_anamoly = algo.ztest(data,"turbidity",turbidity) # Checking for turbidity anamoly
        temp_anamoly = algo.spcc(data,"temperature",temp) # Checking for temperature anamoly 
        #temp_anamoly = algo.ztest(data,"temperature",temp) # Checking for temperature anamoly
        

        # Creating Data Dictionary 
        data = {
            "turbidity":turbidity,
            "temperature":temp,
            "turbidity_anamoly":turbidity_anamoly,
            "temperature_anamoly":temp_anamoly
        }

        firebase.upload(data,timestamp,database) # Upload the data to firebase 
        n = n+1
        time.sleep(delay) # Delay 
    except:
        database = firebase.initialize()
        data = algo.import_df(database)
        turbidity = 1000
        temperature = 1000
        turbidity_anamoly = algo.spcc(data,"turbidity",turbidity) # Checking for turbidity anamoly        
        temp_anamoly = algo.spcc(data,"temperature",temp) # Checking for temperature anamoly 

        timestamp = datetime.datetime.now() # Generating datetime object
        timestamp = int(round(timestamp.timestamp())) # converting datetime object to timestamp
        data = {
            "turbidity":turbidity,
            "temperature":temperature,
            "turbidity_anamoly":turbidity_anamoly,
            "temperature_anamoly":temp_anamoly
        }
        firebase.upload(data,timestamp,database) # Upload the data to firebase 
        print("Anamoly Inserted!")
        n = n+1
        time.sleep(delay) # Delay 



