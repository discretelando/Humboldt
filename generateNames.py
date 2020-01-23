import json
import requests

def generate():
	api_url_base = "https://uinames.com/api/?amount=500&region=united+states"
	response = requests.get(api_url_base)
	if response.status_code == 200:
		return response
	else:
		return None

		
names = generate()
output = json.loads(names.text)
if output is not None:
	with open("generatedNames.csv", 'w', newline='') as file:
		for name in output:
			file.write(name["name"]+","+name["surname"]+"\n")
else:
	print("Error occured")