
import requests

data = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
data.raise_for_status()

data_json = data.json()

question_data=  data_json["results"]