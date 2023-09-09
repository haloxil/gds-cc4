"""
main.py
"""
import json
import urllib.request

def main():
    URL = (
        "https://raw.githubusercontent.com/"
        "Papagoat/brain-assessment/main/restaurant_data.json"
    )
    with urllib.request.urlopen(URL) as response:
        data = json.load(response)

    with open('restaurant.json', 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    return data, metadata