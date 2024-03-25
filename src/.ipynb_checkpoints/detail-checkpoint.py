import requests
import pandas as pd

from typing import Dict


def get_listing_details_by_property_id(api_key: Dict[str, str], property_id:str) -> pd.DataFrame:
    """Get property detail information."""
    
    REALTOR_API_KEY = api_key["REALTOR_API_KEY"]
    url = "https://realtor.p.rapidapi.com/properties/v3/detail"
    querystring = {"property_id":property_id}
    headers = {
    	"X-RapidAPI-Key": REALTOR_API_KEY,
    	"X-RapidAPI-Host": "realtor.p.rapidapi.com"
    }
    listing_details_df = pd.DataFrame()
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        return listing_details_df
    
    listing_details_df = pd.json_normalize(response.json()['data']['home'])
    
    return listing_details_df


def get_nearby_school_info_by_property_id(api_key: Dict[str, str], property_id:str) -> pd.DataFrame:
    """Get nearby school detail information."""
    
    REALTOR_API_KEY = api_key["REALTOR_API_KEY"]
    url = "https://realtor.p.rapidapi.com/properties/v3/detail"
    querystring = {"property_id":property_id}
    headers = {
    	"X-RapidAPI-Key": REALTOR_API_KEY,
    	"X-RapidAPI-Host": "realtor.p.rapidapi.com"
    }
    nearby_schools_df = pd.DataFrame()
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        return nearby_schools_df
    
    nearby_schools_df = pd.json_normalize(response.json()['data']['home']['nearby_schools']['schools'])
    
    return nearby_schools_df



def get_listing_photos_by_property_id(api_key: Dict[str, str], property_id:str) -> list:
    """Get photos of a property."""

    REALTOR_API_KEY = api_key["REALTOR_API_KEY"]
    url = "https://realtor.p.rapidapi.com/properties/v3/get-photos"
    querystring = {"property_id":property_id}
    headers = {
    	"X-RapidAPI-Key": REALTOR_API_KEY,
    	"X-RapidAPI-Host": "realtor.p.rapidapi.com"
    }
    listing_photos = []
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        return listing_photos
    
    listing_photos = [photo['href'] for photo in response.json()['data']['home_search']['results'][0]['photos']]
    
    return listing_photos


def get_listing_surroundings_detail_by_property_id(api_key: Dict[str, str], property_id:str) -> pd.DataFrame:
    """Get surroundings data around a property"""
    
    REALTOR_API_KEY = api_key["REALTOR_API_KEY"]
    url = "https://realtor.p.rapidapi.com/properties/v3/get-surroundings"
    querystring = {"property_id":property_id}
    headers = {
    	"X-RapidAPI-Key": REALTOR_API_KEY,
    	"X-RapidAPI-Host": "realtor.p.rapidapi.com"
    }
    listing_surroundings_detail_df = pd.DataFrame()
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        return listing_surroundings_detail_df
    
    listing_surroundings_detail_df = pd.json_normalize(response.json()['data']['home']['local']['noise']['noise_categories'])
    
    return listing_surroundings_detail_df


def get_drive_commute_time_from_listing(api_key: Dict[str, str], property_id:str, destination_address:str) -> str:
    """Get commute time to travel to a location."""

    REALTOR_API_KEY = api_key["REALTOR_API_KEY"]
    url = "https://realtor.p.rapidapi.com/properties/v3/get-commute-time"
    querystring = {"destination_address":destination_address,"property_id":property_id,"transportation_type":"driving"}
    headers = {
    	"X-RapidAPI-Key": REALTOR_API_KEY,
    	"X-RapidAPI-Host": "realtor.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        return 'commute time unknown'
    
    commute_time = response.json()['data']['home']['commute_time']['duration']['text']
    
    return commute_time




