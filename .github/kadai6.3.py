import requests 

APP_ID = "8b76fe01796bc7e77659cc7284afcb0f9120b48a"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsList?"

params = {
    "appId": APP_ID,
    "limit": 2, # 取得数を2つに制限
    "lang": "J"  # 日本語を指定
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)
