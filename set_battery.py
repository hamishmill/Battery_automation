import requests

def set_battery_charge(value):
# Home Assistant API URL for setting the batter charge value

    light_service_url = "http://10.1.1.125:8123/api/services/number/set_value"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI4ODFlZDE0NzJhMjA0MTM3ODljMzA3YmQxNjBjMjkxOCIsImlhdCI6MTcyODk5ODAyMCwiZXhwIjoyMDQ0MzU4MDIwfQ.AyeTT8kkmdPwDrayd0xk5kWV_VsqFudiitkFuYgGzzA"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

# parameters to go with the action
    data = {
        "entity_id": "number.givtcp_sa2243g060_target_soc" , 
        "value" : value
    }

# Send the POST request to turn on the light
    response = requests.post(light_service_url, headers=headers, json=data)

# Check the response
    if response.status_code == 200:
        print("charge target set")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return