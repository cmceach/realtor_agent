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

def get_home_details_by_property_id(api_key: Dict[str, str], property_id:str) -> pd.DataFrame:
    """Get details home details about 'Heating and Cooling',
                                     'Exterior and Lot Features',
                                     'Land Info',
                                     'Homeowners Association',
                                     'Multi-Unit Info',
                                     'Rental Info',
                                     'Other Property Info',
                                     'Building and Construction',
                                     'Utilities'."""
    
    REALTOR_API_KEY = api_key["REALTOR_API_KEY"]
    url = "https://realtor.p.rapidapi.com/properties/v3/detail"
    querystring = {"property_id":property_id}
    headers = {
    	"X-RapidAPI-Key": REALTOR_API_KEY,
    	"X-RapidAPI-Host": "realtor.p.rapidapi.com"
    }
    home_details_df = pd.DataFrame()
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        return home_details_df
    
    home_details_df = pd.json_normalize(response.json()['data']['home']['details'])
    return home_details_df


def get_property_address_by_property_id(api_key: Dict[str, str], property_id:str) -> dict:
    """Get property address street, city, and postal code information."""

    REALTOR_API_KEY = api_key["REALTOR_API_KEY"]
    url = "https://realtor.p.rapidapi.com/properties/v3/detail"
    querystring = {"property_id":property_id}
    headers = {
        "X-RapidAPI-Key": REALTOR_API_KEY,
        "X-RapidAPI-Host": "realtor.p.rapidapi.com"
    }
    address_dict = {}
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        return address_dict
    
    address_dict = response.json()['data']['home']['location']['address']

    return address_dict

def get_property_history_by_property_id(api_key: Dict[str, str], property_id:str) -> dict:
    """Get property buy/sell history, including 'date', 'event_name', and 'price'."""

    REALTOR_API_KEY = api_key["REALTOR_API_KEY"]
    url = "https://realtor.p.rapidapi.com/properties/v3/detail"
    querystring = {"property_id":property_id}
    headers = {
        "X-RapidAPI-Key": REALTOR_API_KEY,
        "X-RapidAPI-Host": "realtor.p.rapidapi.com"
    }
    property_history_dict = {}
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        return address_dict
    
    property_history_dict = {k:v for k, v in response.json()['data']['home']['property_history'][0].items() if k != 'listing'}

    return property_history_dict


def get_listing_description_by_property_id(api_key: Dict[str, str], property_id:str) -> dict:
    """Get property listing description, including 'baths', 'baths_min', 'baths_max', 'heating', 'cooling', 'beds', 'beds_min', 'beds_max', 'garage', 'garage_min', 'garage_max', 'pool', 'sqft', 'sqft_min', 'sqft_max', 'styles', 'lot_sqft', 'units', 'stories', 'type', 'sub_type', 'listing description', 'year_built', 'name'."""

    REALTOR_API_KEY = api_key["REALTOR_API_KEY"]
    url = "https://realtor.p.rapidapi.com/properties/v3/detail"
    querystring = {"property_id":property_id}
    headers = {
        "X-RapidAPI-Key": REALTOR_API_KEY,
        "X-RapidAPI-Host": "realtor.p.rapidapi.com"
    }
    property_listing_desc_dict = {}
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code != 200:
        return address_dict
    
    property_listing_desc_dict = {k:v for k, v in response.json()['data']['home']['description'].items() if v if not None}

    return property_listing_desc_dict

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




