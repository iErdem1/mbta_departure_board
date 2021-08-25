from logging import basicConfig
from os import stat
from settings import BASE_URL, MBTA_API_KEY
import requests
from datetime import date


class DataFetcher:
    """Creates and get related data"""

    @staticmethod
    def get_api_key():
        return MBTA_API_KEY

    @staticmethod
    def get_baseurl():
        return BASE_URL

    @staticmethod
    def get_schedules_url(trip_id, api_key, base_url):
        return f"{base_url}/schedules?filter[trip]={trip_id}&filter[stop]=place-north&fields[schedule]=departure_time&api_key={api_key}"

    @staticmethod
    def get_predictions_url(api_key,base_url):
        return f"{base_url}/predictions?filter[route_type]=2&filter[stop]=place-north&fields&filter[direction_id]=0&[prediction]=departure_time,status,direction_id,schedule_relationship&api_key={api_key}"

    @staticmethod
    def get_data(url):
        try:
            res = requests.get(url)
            res.raise_for_status()
            data = res.json()['data']
            return data
        except requests.exceptions.HTTPError as err_http:
            raise err_http
        except requests.exceptions.ConnectionError as err_conn:
            raise err_conn
        except requests.exceptions.Timeout as err_timeout:
            raise err_timeout
        except requests.exceptions.RequestException as err_req:
            raise err_req