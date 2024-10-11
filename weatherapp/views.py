from django.shortcuts import render
import requests
import json


# Create your views here.
def get_data():
  url="https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
  params={
    "Authorization":"CWA-84EE207C-D4D1-46E7-A809-0970F6728AD9",
    "format": "JSON",
    "locationName":"臺北市"
  }
  headers = {
        "accept": "application/json"
    }
  response = requests.get(url, params=params,headers=headers)
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

        print("地點："+location)
        print("預測開始時間："+start_time)
        print("預測結束時間："+end_time)
        print("天氣型態："+weather_state)
        print("降雨機率："+rain_prob)
        print("最低氣溫："+min_tem)
        print("氣溫狀態："+comfort)
        print("最高氣溫："+max_tem)

  else:
        print("Can't get data!")

