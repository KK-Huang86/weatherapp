from django.shortcuts import render
import requests

# Create your views here.
def get_data():
  url="https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"
  params={
    "Authorization":"CWA-84EE207C-D4D1-46E7-A809-0970F6728AD9",
    "locationName":"臺北市"
  }
  response = requests.get(url, params=params)
  print(response.status_code)

  if response.status_code == 200:
        # print(response.text)
        data = json.loads(response.text)

        location = data["records"]["location"][0]["locationName"]

        weather_elements = data["records"]["location"][0]["weatherElement"]
        start_time = weather_elements[0]["time"][0]["startTime"]
        end_time = weather_elements[0]["time"][0]["endTime"]
        weather_state = weather_elements[0]["time"][0]["parameter"]["parameterName"]
        rain_prob = weather_elements[1]["time"][0]["parameter"]["parameterName"]
        min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"]
        comfort = weather_elements[3]["time"][0]["parameter"]["parameterName"]
        max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"]

        print(location)
        print(start_time)
        print(end_time)
        print(weather_state)
        print(rain_prob)
        print(min_tem)
        print(comfort)
        print(max_tem)

  else:
        print("Can't get data!")