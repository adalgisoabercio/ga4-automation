
"""UPDATED SOON IF NEEDED AND ALREADY GET ACCESS"""

from apiclient import discovery
from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials
from google.cloud import bigquery
from firebase_admin import credentials, analytics
from google.oauth2.credentials import Credentials
from googleapiclient import build
from datetime import datetime
from typing import List
import firebase_admin
import pandas as pd
import numpy as np
import os



class Google_Play_Console_Data:

    # Replace with your API credentials
    API_KEY = ""
    CLIENT_ID = ""
    CLIENT_SECRET = ""

    def __init__(self, package_name: str, date_range: str, dimensions: list, metrics: list):
        self.package_name = package_name
        self.dimensions = dimensions
        self.metrics = metrics
        self.date_range = date_range
        self.isUpdate = False
        self._data = []

    def check_sheets_nLastDays(self):
        pass

    def request(self):
        # Build the credentials object
        creds = Credentials.from_authorized_user_info(
            info={
                "api_key": self.API_KEY, 
                "client_id": self.CLIENT_ID, 
                "client_secret": self.CLIENT_SECRET
            }
        )

        # Build the Google Play Console API service
        service = build("androidpublisher", "v3", credentials=creds)

        # Replace with the package name of your app
        package_name = "com.example.app"

        # Replace with the track you want to get data for
        track = "alpha"

        # Get the number of new user acquisitions
        # response = service.edits().tracks().patch(
        #     editId = edit_id,
        #     track = track,
        #     packageName = package_name,
        #     body={
        #         "releases": [
        #             {
        #                 "name": release_name,
        #                 "versionCodes": [version_code],
        #                 "status": "completed",
        #                 "userFraction": 1.0,
        #                 "releaseNotes": [
        #                     {
        #                         "language": "en-US",
        #                         "text": "Initial release.",
        #                     },
        #                 ],
        #             },
        #         ],
        #     },
        # ).execute()

        # Replace with the package name of your app
        package_name = "com.example.app"

        # Get the number of ratings for the app
        response = service.reviews().list(
            packageName=package_name,
            maxResults=100,
        ).execute()

        new_user_acquisitions = response["userAcquisitionType"]
        returning_user_acquisitions = response["returningAcquisitionType"]
        ratings = response["reviews"]


class Firebase_Data:

    # CREDS = credentials.Certificate("../api/telkomsel-roli-firebase-adminsdk-pcy21-fbb9448784.json")
    CREDS = service_account.Credentials.from_service_account_file("../api/telkomsel-roli-81ba1cf425eb.json")
    INIT = firebase_admin.initialize_app(CREDS)

    # CLIENT = bigquery.Client.from_service_account_json('../api/telkomsel-roli-81ba1cf425eb.json')
    # DATASET = list(CLIENT.list_datasets())
    # print(DATASET)

    def __init__(self):
        pass

    def check_sheets_nLastDays(self):
        pass

    def request(self):

        start_date = "2022-01-01" # -> Example "2022-01-01"
        end_date = "2022-01-30" # -> Example "2022-11-12"
        response = analytics.get_user_count(start_date = start_date, end_date = end_date)
        # active_users = response.get("total_count")
        print(response)


"""UPDATED SOON IF NEEDED AND ALREADY GET ACCESS"""