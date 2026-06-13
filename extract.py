import os
import requests
import json
from datetime import datetime

def extract_cso_data(table_code):
    """
    Extracts live datasets from the CSO Ireland PxStat API.
    Example table codes: 
    - 'CPM01': Consumer Price Index (Inflation Metrics)
    - 'HPM02': Residential Property Price Index
    """
    print(f"[{datetime.now()}] Starting extraction for CSO Table: {table_code}...")
    
    # Base URL for CSO Ireland PxStat JSON API v1.0
    url = f"https://ws.cso.hra.ie/public/api.restful/PxStat.Data.Cube_v1.0/ReadDataset/{table_code}/JSON-stat/2.0/en"
    
    try:
        response = requests.get(url, timeout=30)
        
        # Check if the API request was successful (Status Code 200)
        response.raise_for_status()
        
        # Define storage path
        raw_data_dir = os.path.join(os.path.dirname(__file__), '../data')
        os.makedirs(raw_data_dir, exist_ok=True)
        
        filename = f"{table_code}_raw_{datetime.now().strftime('%Y%m%d')}.json"
        filepath = os.path.join(raw_data_dir, filename)
        
        # Save the raw JSON data to our data folder
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)
            
        print(f"[{datetime.now()}] Success! Raw data saved to: {filepath}")
        return filepath

    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now()}] Error extracting data from CSO API: {e}")
        return None

if __name__ == "__main__":
    # Targeting the Consumer Price Index (CPM01) for inflation metrics
    target_table = "CPM01" 
    extract_cso_data(target_table)
