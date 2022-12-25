import pandas as pd

def update_to_engagement_sheet(self, sheets_id: str):
        engagement_realtime_data = [{
            'Date': '',
            'New User\nAcquistions': '',
            'Returning User\nAcquisitions': '',
            'All User\nAcquisitions': '',
            'All User\nLoss': '',
            'DAU': '',
            'MAU': '',
            'Total Install': '',
            'Total New User\nAcquistions': '',
            'Total All User\nAcquistions': '',
            'Total All User\nLoss': '',
            'App\nStickiness': '',
            'Retention\nRate': '',
            'Churn Rate': '',
            'Google Play\nRating': '',
            'Visitors': '',
            'Views to Install': '',
            'Conversion Rate': '',
            'Audience Growth Rate\nAll Audience': ''
        }]

        df = pd.DataFrame(engagement_realtime_data)
        save_file = df.to_csv('data/engagement_example.csv', index=False)
        print("OK!!")

def update_to_loss_sheet(self, sheets_id: str):
    loss_realtime_data = {
        'Date' : '',
        'App Version' : '',
        'Crash' : '',
        'Crash\n1000 Devices' : '',
        'ANR' : '',
        'ANR\n1000 Devices' : ''
    }

    df = pd.DataFrame(loss_realtime_data)
    save_file = df.to_excel('data/loss_example.xlsx', index = False)
    print("OK!!")

# report = Google_Analytics_Data()
    # new_report = report.request(
    #     
    #     dimensions = ['date', 'unifiedScreenClass'],
    #     metrics = ['activeUsers', 'screenPageViews'],
    #     date_range = ['2022-12-21', '2022-12-21']
    # )

    # to_excel = excel_import(
    #     dimensions = ['date', 'unifiedScreenClass'],
    #     metrics = ['activeUsers', 'screenPageViews'],
    #     date_range = ['2022-12-21', '2022-12-21'],
    # )

# df = pd.DataFrame(to_excel)
    # save_file = df.to_excel('user_activity.xlsx')
    # print("OK!!")
    # print(new_report)