from flask import Flask, render_template
from train import Train
from data_fetcher import DataFetcher
from parser import Parser


app = Flask(__name__)


@app.route("/departure_board")
def departure_board():
    train_list = []
    data_fetcher = DataFetcher()
    parser = Parser()
    api_key = data_fetcher.get_api_key()
    base_url = data_fetcher.get_baseurl()
    prediction_url = data_fetcher.get_predictions_url(api_key=api_key,base_url=base_url)
    prediction_data = data_fetcher.get_data(prediction_url)
    #time.sleep(0.3)
    for train in prediction_data:
        direction_id = parser.get_direction_id(train)
        trip_id = parser.get_trip_id(train)
        trip_data = parser.get_trip_detail(trip_id,base_url)
        #time.sleep(0.2)
        status = parser.get_status(train)
        departure_time = parser.get_departure_time(train, trip_id,api_key,base_url)
        destination = parser.get_destination(trip_data)
        train_number = parser.get_train_number(trip_data)

        train_obj = Train(
            departure_time=departure_time,
            direction_id=direction_id,
            destination=destination,
            train_number=train_number,
            status=status
        )
        train_list.append(train_obj)
        train_list.sort()
    return render_template(
        "departure_board.html", context=train_list)

if __name__ == "__main__":
    app.run(debug=True)