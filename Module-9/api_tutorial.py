"""
Daniel Vance
CSD-325
Module 9 – APIs

This program demonstrates how to connect to the Open Notify API,
check the status of the connection, retrieve JSON data,
and format the output for readability.
"""

import requests
import json

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    
    print("\nNumber of astronauts in space:", data["number"])
    print("\nAstronauts currently in space:\n")
    
    for person in data["people"]:
        print(person["name"], "-", person["craft"])
else:
    print("Failed to connect to API.")