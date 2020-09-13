import requests
import json
token = ''
steamid64 = input("Enter SteamID64: ") 
url = 'https://steamladder.com/api/v1/profile/' + steamid64
headers = {'Authorization': 'Token ' + token}
receive=requests.get(url, headers=headers)
jsonn = json.loads(receive.text)
user = jsonn["steam_user"]["steam_name"]
playtime_hr = round(jsonn["steam_stats"]["games"]["total_playtime_min"] / 60)
print("\n|RAW|\n" + receive.text + "\n\n|PARSED|\nUser Name:\n" + user + "\nLevel:\n" + str(jsonn["steam_stats"]["level"]) + "\nPlaytime (Minutes):\n" + str(jsonn["steam_stats"]["games"]["total_playtime_min"]) + "\nPlaytime (Hours):\n" + str(playtime_hr))
