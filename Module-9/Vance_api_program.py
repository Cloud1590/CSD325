"""
Daniel Vance
CSD-325
Module 9 – APIs

This program demonstrates how to connect to the open-meteo API,
check the status of the connection, retrieve JSON data,
and format the output for readability.
"""

import requests
import json

# Omaha, NE coordinates
url = "https://api.open-meteo.com/v1/forecast?latitude=41.2565&longitude=-95.9345&current_weather=true"

response = requests.get(url)

# 1. Test connection
print("Status Code:", response.status_code)

# 2. Print raw response
print("\nRaw Response:")
print(response.text)

# 3. Print formatted response
if response.status_code == 200:
    data = response.json()
    
    print("\nFormatted Weather Output:")
    print("Temperature:", data["current_weather"]["temperature"], "°C")
    print("Wind Speed:", data["current_weather"]["windspeed"], "km/h")
    print("Wind Direction:", data["current_weather"]["winddirection"], "degrees")
else:
    print("Connection failed.")