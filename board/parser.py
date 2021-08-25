import requests
from data_fetcher import DataFetcher


class Parser:
    @staticmethod
    def get_direction_id(prediction_data):
        """Direction ID must be 0 for departures from North Station"""
        direction_id = prediction_data['attributes']['direction_id']
        return direction_id

    @staticmethod
    def get_departure_time(data,trip_id,api_key,base_url):
        departure_time = data['attributes']['departure_time']
        if departure_time != None:
            formatted_dt = departure_time[11:-6]
            return formatted_dt
        scheduled_url = DataFetcher().get_schedules_url(trip_id,api_key=api_key,base_url=base_url)
        scheduled_data = DataFetcher().get_data(scheduled_url)[0]
        departure_time = scheduled_data['attributes']['departure_time']
        formatted_dt = departure_time[11:-6] #Quick solution to format departure time.
        return formatted_dt

    @staticmethod
    def get_trip_id(data):
        """To get headsign, destination, track number and train number"""
        trip_id = data['relationships']['trip']['data']['id']
        return trip_id
    
    @staticmethod
    def get_trip_detail(id,base_url):
        url = f'{base_url}/trips?filter[id]={id}'
        res = requests.get(url=url)
        data = res.json()['data']
        return data
    
    @staticmethod
    def get_destination(data):
        destination = data[0]['attributes']['headsign']
        return destination
    
    @staticmethod
    def get_train_number(data):
        train_number = data[0]['attributes']['name']
        return train_number

    @staticmethod
    def get_status(prediction_data):
        status = prediction_data['attributes']['status']
        return status
