import requests
import json
from datetime import date, timedelta
import numpy as np
import pandas as pd

def get_weekly_average():
    
    API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NTc3MDIxOS1jYWE2LTRmOTctOTE3Ni0zNDBlZGMzZDQxNTgiLCJqdGkiOiIyMDM2ZjZjMWE4MGNjODk0YTI0MTZlM2Y2ODEwYTA3ZThmNTk2YjY1ZmQ5ZDFhOTE0MGY0OTg1ZThjOWU5M2JiOTVmZTVmMzlhNjI1Y2NmZSIsImlhdCI6MTcyNjgzMTQ5OC45NzMxNzUsIm5iZiI6MTcyNjgzMTQ5OC45NzMxNzksImV4cCI6MTc1OTIzMTQ5OC45NjY3NTksInN1YiI6IjM1MDk0Iiwic2NvcGVzIjpbImFwaTphY2NvdW50IiwiYXBpOm5vdGlmaWNhdGlvbiIsImFwaTpldi1jaGFyZ2VyOmRhdGEiLCJhcGk6ZXYtY2hhcmdlcjpsaXN0IiwiYXBpOmV2LWNoYXJnZXI6cmVhZCIsImFwaTppbnZlcnRlcjpkYXRhIiwiYXBpOmludmVydGVyOmxpc3QiLCJhcGk6aW52ZXJ0ZXI6cmVhZCIsImFwaTpzaXRlOmxpc3QiLCJhcGk6c2l0ZTpyZWFkIiwiYXBpOnNtYXJ0LWRldmljZTpkYXRhIiwiYXBpOnNtYXJ0LWRldmljZTpsaXN0IiwiYXBpOnNtYXJ0LWRldmljZTpyZWFkIl19.dxnsMs--Ld-nU5BmeLchDXzJ-DuOTlhzBX9xSO83XU6cU0qa2T324V5SFN_evPXUkuWeRJxWLgyJvyaPIUtHmw08lSSXGmbzP00itdk7vik27OqjPI2mOojq2qY9MFMxkpWo9uq9xJyhnyEK2dqxphZwOdqeA7d41EXL5o5umcSvinmyGqhOpJVP4oTDJ6b3WYLsD9UlQGfIFQzI5N0TxLVCINTmln4HEa4zma8RjGkv9qJBQJWc7V_w6jwMrs_RbWZYvsGhCj1ILxOlAxRcPF5aZg2MuSRFh2Ty9W5K4AefLE31pGdnH2eeFlYv6Oqm_nIJbCkHboIMCoTgNMMAC4ZlcgCmxxCQ9krq9Fc3xE4X-HOyfQW4_3zN8GkGXbiTFNBft5nbb3RArjPtF3V6q05t4uTWf2mBDuDPJXpGMUSO9pLSGbTSgedn--k1qal7nlB44IxXzOAGaTlKmyyjij6-QhDoypnoucAcWoRUz58tjlzdZHO00Qzyz4dTaBSahgEe4e4AvBi8c8UZ2H2gSO_87X8aU4HBHDNeJzX_ehs2x_7sVNmwCAhr2iqKKinZCJsRPX6o6J0ZZCe7m_RwpnFc13VQWuI8jbuKCdlo1L1noqVvSYPYj8G5_gi3oiVqdQysT1dVZoR6z3FLalEciqWtXqdkqEyIXjBljMEsPek'
# Set the inverter serial number and the date
    inverter_serial_number = 'SA2243G060'  # Replace with your inverter's serial number
    

    def fetch_data_points(api_key, inverter_serial, day):
        base_url = f'https://api.givenergy.cloud/v1/inverter/{inverter_serial}/data-points/{day}'
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
        page = 1
        all_data = []
        #while true to loop through all pages for the day.
        while True:
            params = {
                'page': page
            }
        
            response = requests.get(base_url, headers=headers, params=params)

            if response.status_code == 200:
                data = response.json()
                all_data.extend(data['data'])  # Add the new data to our list
                page += 1  # Move to the next page
                #print(page)
            if not data['data']:
                break
    
        return all_data

    today = date.today()

    num_days = 1 
    #which previous date we want to look at
    day = today - timedelta(days = num_days)

    daily_totals = [0] * 7

    for i in range(0,7):
        #set initial date
        day = today - timedelta(days = num_days)
        #creates the json data response
        historic_givenergy_data = fetch_data_points(API_KEY, inverter_serial_number, day)
        #turns the json data into a pandas df
        historic_givenergy_dataframe = pd.json_normalize(historic_givenergy_data)
        #selects the value for total energy consumption in the house for that day and stores in a list
        daily_totals[i] = historic_givenergy_dataframe['today.consumption'].iloc[-1]

        num_days += 1
        print(num_days)

    return daily_totals