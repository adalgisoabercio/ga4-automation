from Automation import Google_Analytics_Data, Google_Sheets_Config
import pandas as pd


def main(): 

    print("""Welcome to Google Analytics Automations for roli Performance""")
    choice = int(input("""
        Choose your action : 
        1. Save Data from Google Sheets
        2. Get and Save Data from Google Analytics
        3. Updating the Data (Update Soon)
        4. Delete the Data (Update Soon)
        
        Your Choice : """))

    if choice == 1:
        
        # Updating the Worksheet
        worksheet_name = input("Which worksheet that you want to save : ")
        get_worksheets = Google_Sheets_Config(f'{worksheet_name}')

        file_name = input("The File Name : ")
        download = get_worksheets.download_sheets(file_name)
        print(download)

    if choice == 2:
        print("The Input in string format with comma separated. No Space needed\n")

        # Google Analytics 4 Dimensions and Metrics API -> https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema
        dimensions_input = list(map(str, input("Dimensions : ").split(',')))
        metrics_input = list(map(str, input("Metrics : ").split(',')))
        date_input = list(map(str, input("Date Range : ").split(',')))

        # The Google Analytics request instances
        ga4_data = Google_Analytics_Data()
        
        # run the request
        request = ga4_data.request(
            dimensions = dimensions_input,
            metrics = metrics_input,
            date_range = date_input
        )

        file = pd.DataFrame(request)
        file_name = input("\nWhat's file name : ")
        save = file.to_csv(f'data/{file_name}.csv', index = False)
        print(f'{file_name}.csv already saved')


    if choice == 3:
        print("""IN FURTHER NEEDS AND OPPORTUNITIES""")

        pass


    if choice == 4:
        print("""IN FURTHER NEEDS AND OPPORTUNITIES""")

        pass


if __name__ == '__main__':
    main()