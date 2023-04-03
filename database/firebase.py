import pyrebase
from google.oauth2 import service_account
import firebase_admin
from firebase_admin import credentials

def initialize():

    config = {
        "apiKey": "AIzaSyCQh-8hZ-d8GL3lyCQYTxlOaRig1XDDJFQ",
        "authDomain": "tarp-e8fb8.firebaseapp.com",
        "projectId": "tarp-e8fb8",
        "storageBucket": "tarp-e8fb8.appspot.com",
        "messagingSenderId": "431841665583",
        "appId": "1:431841665583:web:eb8b3116cf8cd55857dcda",
        "measurementId": "G-Z074KBKY7N",
        
        "databaseURL": "https://tarp-e8fb8-default-rtdb.firebaseio.com/"
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



