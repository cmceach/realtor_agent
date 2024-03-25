import requests
import pandas as pd

from typing import Dict


def get_listings_by_postal_code(api_key: Dict[str, str], postal_code:str) -> pd.DataFrame:
    """List properties for sent, sale, sold with options and filters"""
    
    REALTOR_API_KEY = api_key["REALTOR_API_KEY"]
    url = "https://realtor.p.rapidapi.com/properties/v3/list"
    payload = {
    	"limit": 200,
    	"offset": 0,
    	"postal_code": postal_code,
    	"status": ["for_sale", "ready_to_build"],
    	"sort": {
    		"direction": "desc",
    		"field": "list_date"
    	}
    }
    headers = {
    	"content-type": "application/json",
    	"X-RapidAPI-Key": REALTOR_API_KEY,
    	"X-RapidAPI-Host": "realtor.p.rapidapi.com"
    }    
    listings_df = pd.DataFrame()
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        return listings_df

    listings_df = pd.json_normalize(response.json()['data']['home_search']['results'])
    
    return listings_df


def get_similar_listings_by_property_id(api_key: Dict[str, str], property_id:str) -> pd.DataFrame:
    """Find similar homes given the property_id."""
    
    REALTOR_API_KEY = api_key["REALTOR_API_KEY"]
    url = "https://realtor.p.rapidapi.com/properties/v3/list-similar-homes"
    querystring = {"property_id":property_id,"limit":"10","status":"for_sale"}
    headers = {
    	"X-RapidAPI-Key": REALTOR_API_KEY,
    	"X-RapidAPI-Host": "realtor.p.rapidapi.com"
    }
    similar_listings_df = pd.DataFrame()
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        return similar_listings_df

    similar_listings_df = pd.json_normalize(response.json()['data']['home']['related_homes']['results'])
    
    return similar_listings_df









