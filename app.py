from chalice import Chalice
from requests.auth import HTTPBasicAuth
import requests
import json

auth = HTTPBasicAuth('apikey', 'API_KEY')
url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,XRP,DASH,ADA&tsyms=USD"

app = Chalice(app_name='hellolambda')


@app.route('/')
def index():
    try:
        response =  requests.get(url, auth=auth)

        return json.loads(response.text)
    except Exception as e:
        return {'exception': e.message}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
