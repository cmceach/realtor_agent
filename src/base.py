from typing import List, Optional, Any, Dict
from . import autocomplete, listing, detail
import pandas as pd
from datetime import datetime, timedelta
from llama_index.core.tools.tool_spec.base import BaseToolSpec


class RealtorAgentToolSpec(BaseToolSpec):
    spec_functions = [
        "get_property_id",
        "get_listings_by_postal_code",
        "get_similar_listings_by_property_id",
        "get_listing_details_by_property_id",
        "get_nearby_school_info_by_property_id",
        "get_listing_photos_by_property_id",
        "get_listing_surroundings_detail_by_property_id",
        "get_drive_commute_time_from_listing"
    ]

    def __init__(
        self,
        realtor_api_key: str
    ):
        self._api_key = {
            "REALTOR_API_KEY": realtor_api_key,
        }

    def get_property_id(self, address: str) -> str:
        """Given a property address, returns the property id."""
        return autocomplete.get_property_id(self._api_key, address)

    def get_listings_by_postal_code(self, postal_code: str) -> pd.DataFrame:
        """Given a postal code, returns a dataframe of properties for sale and their characteristics."""
        return listing.get_listings_by_postal_code(self._api_key, postal_code)

    def get_similar_listings_by_property_id(self, property_id: str) -> pd.DataFrame:
        """Given a property id, returns a dataframe of similar properties and their characteristics."""
        return listing.get_similar_listings_by_property_id(self._api_key, property_id)

    def get_listing_details_by_property_id(self, property_id: str) -> pd.DataFrame:
        """Given a property id, returns a dataframe of the property's characteristics."""
        return detail.get_listing_details_by_property_id(self._api_key, property_id)

    def get_nearby_school_info_by_property_id(self, property_id: str) -> pd.DataFrame:
        """Given a property id, returns a dataframe of the property's characteristics."""
        return detail.get_nearby_school_info_by_property_id(self._api_key, property_id)

    def get_listing_photos_by_property_id(self, property_id: str) -> list:
        """Given a property id, returns a list of photo links for the property."""
        return detail.get_listing_photos_by_property_id(self._api_key, property_id)

    def get_listing_surroundings_detail_by_property_id(self, property_id: str) -> pd.DataFrame:
        """Given a property id, returns a dataframe of details on the area surrounding the property"""
        return detail.get_listing_surroundings_detail_by_property_id(self._api_key, property_id)

    def get_drive_commute_time_from_listing(self, property_id: str, destination_address:str) -> str:
        """Given a property id and destination address, returns a string describing the driving commute time"""
        return detail.get_drive_commute_time_from_listing(self._api_key, property_id, destination_address)