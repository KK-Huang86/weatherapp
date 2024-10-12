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

        line_notify(tuple([location, start_time, end_time,
                           weather_state, rain_prob, min_tem, comfort, max_tem]))
        print("--------")

  else:
        print("Can't get data!")


def line_notify(data):


  token="vw4wkwLx1bBxNtVaqdyGrGnTiwZax5xKfimkPxOMOEd"
  message = ""

  if len(data)==0:
      message+= "\n[Error] 無法取得天氣資訊，請稍後再試"

  else:
        message += f"\n今天{data[0]}的天氣: {data[3]}\n"
        message += f"溫度: {data[5]}°C - {data[7]}°C\n"
        message += f"降雨機率: {data[4]}%\n"
        message += f"舒適度: {data[6]}\n"
        message += f"天氣預估時間: {data[1]} ~ {data[2]}\n"

  line_url = "https://notify-api.line.me/api/notify"
  line_header = {
        "Authorization": 'Bearer ' + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
  line_data = {
        "message": message
    }

  requests.post(url=line_url, headers=line_header, data=line_data)


if __name__ == '__main__':
  get_data()
  line_notify()
