import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Create your views here.
def get_data():
  url="https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"
  params={
    "Authorization":os.getenv("Authorization"),
    "format": "JSON",
    "locationName":"臺北市"
  }
  headers = {
        "accept": "application/json"
    }
  response = requests.get(url, params=params,headers=headers)
  # print(response.status_code)

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

        # print("地點："+location)
        # print("預測開始時間："+start_time)
        # print("預測結束時間："+end_time)
        # print("天氣型態："+weather_state)
        # print("降雨機率："+rain_prob)
        # print("最低氣溫："+min_tem)
        # print("氣溫狀態："+comfort)
        # print("最高氣溫："+max_tem)

        return (location, start_time, end_time, weather_state, rain_prob, min_tem, comfort, max_tem)

     

  else:
        print("Can't get data!")
        return None


def line_notify(data):


  token=os.getenv("line_notify_token")
  message = ""

  if len(data)==0:
      message+= "\n[Error] 無法取得天氣資訊，請稍後再試"

  else:
        message += f"\n今天{data[0]}的天氣: {data[3]}\n"
        message += f"溫度: {data[5]}°C - {data[7]}°C\n"
        message += f"降雨機率: {data[4]}%\n"
        message += f"舒適度: {data[6]}\n"
    
        if int(data[4])>70:
          message+= "提醒您，今天有可能會下雨，出門前記得帶傘\n"
        elif int(data[7])>32:
          message += "提醒您，今天天氣炎熱，請記得多補充水分\n"
        elif int(data[5])<10:
          message +="提醒您，今天天氣寒冷，請記得多穿一點"
        elif int(data[7]) - int(data[5]) > 10:
          message +="提醒您，今天天氣變化大，請多注意保暖"


        message += f"天氣預估時間: {data[1]} ~ {data[2]}\n"

  line_url = "https://notify-api.line.me/api/notify"
  line_header = {
        "Authorization": 'Bearer ' + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
  line_data = {
        "message": message
    }

  response=requests.post(url=line_url, headers=line_header, data=line_data)
  print(f"Status code: {response.status_code}")



if __name__ == '__main__':
  get_data()