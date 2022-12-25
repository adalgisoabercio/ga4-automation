# Google Analytics 4 Automations Data for roli Performance Dashboard

## MAKE SURE THE ACCOUNT ALREADY CAN ACCESSED TO GOOGLE CLOUD PLATFORM AND GOOGLE DEVELOPERS

### OFFICIAL References Links:
1. [API QUICKSTART](https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries)
2. [Google Analytics Data API OVERVIEW](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/?apix=true)
3. [v1beta Google Analytics API Properties](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties)
4. [Google Analytics 4 Dimensions and Metrics](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema)
5. [Google Cloud Client Libraries for google-analytics-data (Beta Analytics Data Client)](https://googleapis.dev/python/analyticsdata/latest/data_v1beta/beta_analytics_data.html#google.analytics.data_v1beta.services.beta_analytics_data.BetaAnalyticsDataClient)
6. [RunReportRequest()](https://googleapis.dev/python/analyticsdata/latest/data_v1beta/types.html#google.analytics.data_v1beta.types.RunReportRequest)
7. [Official Google API Repositories](https://github.com/googleapis/google-api-python-client)

### More References Links
1. https://github.com/tanyazyabkina/GA4_API_python/blob/main/GA4%20Python%20Report.ipynb



### The overview of the process:
1. Get API keys: create a GCP project, authorize Google Analytics Data API, create a service account, create JSON keys for the account.
2. Add service account as a viewer to your GA4 property
    - Admin -> Account Access Management, 
    - Properties -> Property Access Management
3. Install google-analytics-data package.
4. Set os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'your_api_key.json'
5. Send request, get output. Done!

### Managing Virtual Environment and Libraries
1. Installing python-pipenv
    ```
    pip install python-pipenv
    ```
2. Creating Virtual Enviroment
    ```
    pipenv shell
    ```
3. Downloading and Installing the Libraries from requirements.txt
    ```
    pipenv install -r ./requirements.txt
    ```
4. Creating and Saving some libraries (if updated, deleted, and et cetera) to requirements.txt
    ```
    pipenv lock -r > requirements.txt
    ```

### Dimensions and Metrics Template
```
req = ga.request(
    dimensions = ['date','unifiedScreenClass'],
    metrics = ['activeUsers'],
    date_range = ['2022-01-01','today']
)
```