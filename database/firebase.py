import pyrebase
from google.oauth2 import service_account
import firebase_admin
from firebase_admin import credentials

def initialize():

    config = {
        "apiKey": "<API KEY>",
        "authDomain": "<authDomain>",
        "projectId": "<projectId>",
        "storageBucket": "<storageBucket>",
        "messagingSenderId": "<messagingSenderId>",
        "appId": "<appId>",
        "measurementId": "<measurementId>",
        
        "databaseURL": "<databaseURL>"
    }

    firebase = pyrebase.initialize_app(config) 
    database = firebase.database()
    return database


def upload(data,time_stamp,database):
    database.child(time_stamp).set(data)
    return

def read(database):
    data = database.get()
    return data



