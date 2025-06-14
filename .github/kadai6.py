import requests

API_ID = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m&timezone=Asia/Tokyo"

requests = requests.get(API_ID)

if response.status_code == 200:
    data = response.json()  #jsonコード取得

    temperature = data['hourly']['temperature_2m'][0] #APIから情報を取得

    print(f'現在の気温は{temperature}度です。') #気温を表示
else:
    print(f"データ取得に失敗しました。{response.status_code}") #失敗の時表示
