import requests
import pandas as pd

from typing import Dict


def get_property_id(api_key: Dict[str, str], address:str) -> str:
    """Given a property address, returns a property id"""
    
    REALTOR_API_KEY = api_key["REALTOR_API_KEY"]
    url = "https://realtor.p.rapidapi.com/locations/v2/auto-complete"
    querystring = {"input":address, "limit":"10"}
    headers = {
    	"X-RapidAPI-Key": REALTOR_API_KEY,
    	"X-RapidAPI-Host": "realtor.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        return ''

    location_metadata_df = pd.json_normalize(response.json()['autocomplete'])
    property_id = str(location_metadata_df[location_metadata_df['area_type'].eq('address')]['mpr_id'].values[0])
    
    return property_id