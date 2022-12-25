"""
    THE roli Performance Data Resources Wrangling

    author          = roli Telkomsel
    Date Released   = December 23, 2022
    Version         = v1.0.0
"""


from api.ROLi_API import ROLi_Google_API # API and Service Account Secret Informations
from oauth2client.service_account import ServiceAccountCredentials # Service Account Credetials Authentication Library
from google.analytics.data_v1beta import BetaAnalyticsDataClient # Google Cloud Client Libraries for Google Analytics 4
from google.analytics.data_v1beta.types import ( DateRange, Dimension, Metric, RunReportRequest, OrderBy )
from datetime import datetime,time
import gspread as Spreadsheet # Google Spreadsheets Utilities Library with Google Sheet API
import pandas as pd
import os


class Google_Analytics_Data:

    # Credentials Instances from Service Account JSON File
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ROLi_Google_API.SERVICE_ACCOUNT

    def __init__(self):
        
        """Google Analytics Automations Utilities for roli Performance Dashboard"""

        self.property_id = ROLi_Google_API.GOOGLE_ANALYTICS_PROPERTY_ID
        self._data = []
        self.lastDays = ""


    def __repr__(self) -> str:
        data_info =  ""


    def request(self, dimensions: list, metrics: list, date_range: list) -> None:
        """
        Sending the request to Google Anlaytics API for retrieve data
        :param list dimension   : The suggested of Google Analytics 4 Dimensions API
        :param list metrics     : The suggested Google Analytics 4 Metrics API
        :param list date_range  : Suggested Google Analytics 4 date ranges

        :type priority          : DataFrame
        :return                 : The suggested GA4 Data
        """

        # The dimension list
        dimension_list = [Dimension(name = dimension) for dimension in dimensions]

        # The metric list
        metric_list = [Metric(name = metric) for metric in metrics]

        # Run the Request Instances; The Important Dimensions, Metrics, Order, and Date Ranges that want to retrieve
        roli_report = RunReportRequest(
        
            property = f'properties/{self.property_id}',
            dimensions = dimension_list, 
            metrics = metric_list,         
            order_bys = [OrderBy(dimension = {'dimension_name' : 'date'})],
            date_ranges = [DateRange(start_date = f'{date_range[0]}', end_date = f'{date_range[1]}')],
            limit = 100000,
        )

        # Instantiates the beta analytics data client.
        response = BetaAnalyticsDataClient().run_report(roli_report)
        
        # The Set Up for data name
        row_index_names = [header.name for header in response.dimension_headers]
        metric_names = [header.name for header in response.metric_headers]

        # Store the all dimension name to row header from request 
        row_header = []
        for i in range(len(row_index_names)):
            row_header.append(
                [row.dimension_values[i].value for row in response.rows]
            )

        # Changing the date type from <class 'str'> to suggested date format
        row_header[0] = pd.to_datetime(row_header[0], format = '%Y%m%d')
        
        # Store the all data values from request
        data_values = []
        for i in range(len(metric_names)):
            data_values.append([row.metric_values[i].value for row in response.rows])

        # Combining the all recorded data into DataFrame
        dt = pd.DataFrame(row_header + data_values)

        # return the transpose of DataFrame
        return dt.T
    
    def check_sheets_nLastDays(self) -> str:

        #  Google Sheets Class Instances
        sheet_instances = Google_Sheets_Config()

        # Get the last recorded date from selected worksheet
        get_last_day = sheet_instances.getNLastDays()

    
    def updating_data(self) -> str:
        pass




class Google_Sheets_Config:

    # Credentials Instances from Service Account JSON File and scope configutations
    CREDS = ServiceAccountCredentials.from_json_keyfile_name(
        ROLi_Google_API.SERVICE_ACCOUNT, 
        ROLi_Google_API.SCOPE)

    # Authorize the Spreadsheet with gspread library, and open the selected spreadsheet by ID
    CLIENT = Spreadsheet.authorize(CREDS)
    SPREADSHEET = CLIENT.open_by_key(ROLi_Google_API.SHEET_ID)

    def __init__(self, selected_worksheet: str) -> None:
        """
        Google Sheets Utilities for roli Performance Data

        :param str selected_worksheet   : Parsing the suggested worksheet. The Worksheet already on Spreadsheets
        :type priority          : None
        """

        self.selected_worksheet = self.SPREADSHEET.worksheet(selected_worksheet)
        self.isUpdate = False
        self.date_range = ""
        self.nLastDay = ""

    def get_worksheet_access(self) -> None:
        """Accessing and Getting all recorded values from Google Sheets"""

        # Get the all values from selected worksheet
        sheet = self.selected_worksheet.get_all_values() # worksheet(f'{self.selected_worksheet}')

        # return the DataFrame of selected worksheet values
        return pd.DataFrame(sheet)

    def getNLastDays(self) -> str:
        """Retrieve the last recorded date in selected worksheets"""
        
        # Get the last recorded date data
        sheet_last_day = self.get_worksheet_access()[0].iloc[-1]
        
        # Check if self.nLastDay is lower sheet_last_day from selected worksheet
        # if lower, then update the self.nLastDay by sheet_last_day
        if self.nLastDay < sheet_last_day: self.date_range = sheet_last_day

        # return the last day for the class
        return self.nLastDay

    def creating_sheets(self, sheet_name: str) -> str:
        """
        Creating a New Worksheet in current Sheets

        :param str sheet_name   : The selected worksheet. The Worksheet already on Spreadsheets
        :type priority          : str
        :return                 : creating a new worksheet
        """

        # Declare for creating a new worksheet
        new_worksheet = self.SPREADSHEET.add_worksheet(sheet_name)

        # Updating the worksheet name from class to the new created worsheet name
        self.selected_worksheet = new_worksheet

        # return the success informations
        return f'{self.selected_worksheet} is sucessfully created !!'


    def updating_sheets(self, request_data) -> bool:
        """
        Automatically updating the selected worksheet data from requesting and resources
        
        :param DataFrame request_data  : The requested data. Google Analytics 4 / Firebase / ...
        :type priority                 : bool
        :return                        : The worksheets already updated
        """

        # while the recorded data is less than the newest date from selected worksheet
        while self.nLastDay < self.getNLastDays():
            
            self.nLastDay = self.getNLastDays()
            
            update = self.selected_worksheet.update('A1', request_data)
            
            # Update is True
            self.isUpdate = True

        return time(update)

    
    def download_sheets(self, sheet_name: str) -> str:
        """
        Downloading the selected worksheets to local drive
        
        :param str sheet_name   : The selected worksheet. The worksheet already on Spreadsheets
        :type priority           : str
        :return                  : file success saved.
        """

        # Save the selected worksheets to an excel file, with no index
        save = self.get_worksheet_access().to_csv(
            f'data/{sheet_name}.csv', 
            index = False
        )

        # return success informations
        return f'File {sheet_name}.csv succesfully saved !'


    def deleting_sheets(self, sheet_name: str) -> str:
        """
        Deleting the suggested worksheet(s)
        """
        pass

class Automation_Interface:

    WIDTH = 800
    HEIGHT = 920

    def __init__(self):
        self.x = 8
        self.y = 10

    def record_request(self):
        pass