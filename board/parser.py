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
    def get_trip_detail(trip_id,base_url):
        try:
            url = f'{base_url}/trips?filter[id]={trip_id}'
            res = requests.get(url=url)
            data = res.json()['data'][0]
            return data
        except KeyError:
            print("API data broken.")
    
    @staticmethod
    def get_destination(data):
        try:
            destination = data['attributes']['headsign']
            return destination
        except TypeError:
            destination = "Loading..."
            print("NoneType Error. Trip Data broken.")
            return destination   
    @staticmethod
    def get_train_number(data):
        try:
            train_number = data['attributes']['name']
            return train_number
        except TypeError:
            destination = "Loading..."
            print("NoneType Error. Trip Data broken.")
            return destination

    @staticmethod
    def get_status(prediction_data):
        status = prediction_data['attributes']['status']
        return status
