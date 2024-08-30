import json
import requests
def lakatsiya_aniqlash(shahar):
	url = "https://geocoding-by-api-ninjas.p.rapidapi.com/v1/geocoding"
	querystring = {"city": f"{shahar}"}
	headers = {
		"x-rapidapi-key": "74e87e6a9bmsh3a53f3a52ddfeb5p15a652jsn40c8ada09ec1",
		"x-rapidapi-host": "geocoding-by-api-ninjas.p.rapidapi.com"
	}
	response = requests.request("GET",url, headers=headers, params=querystring)
	if response.status_code==200:
		data=json.loads(response.text)
		lati=data[0]['latitude']
		long=data[0]['longitude']
		loc=[lati,long]
		return loc
	else:
		return "Error"
def obhavo(shahar):
	url = "https://weatherapi-com.p.rapidapi.com/current.json"

	querystring = {"q": f"{shahar[0]},{shahar[1]}"}

	headers = {
		"x-rapidapi-key": "74e87e6a9bmsh3a53f3a52ddfeb5p15a652jsn40c8ada09ec1",
		"x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
	}

	response = requests.request("GET",url, headers=headers, params=querystring)

	if response.status_code==200:
		data=json.loads(response.text)
		info=(
			f"shahar:{data['location']['name']}\n"
			f"davlat:{data['location']['country']}\n"
			f"vaqt mintaqasi:{data['location']['tz_id']}\n"
			f"havo harorati{data['current']['last_updated']} holatida "
			f" {data['current']['temp_c']}°C\n"
		)
		return info
	else:
		return "Error"