import requests
import datetime

#Check latest graph here https://pixe.la/v1/users/faithisaunicorn/graphs/graph-1.html

PIXELA_ENDPOINT = "https://pixe.la/v1/users/faithisaunicorn/graphs"

USERNAME = "faithisaunicorn"
TOKEN = "X"

PARAS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

###TODO: Create account (only need to run this once)
# response = requests.post(url="https://pixe.la/v1/users", json=PARAS)
# print(response.text)

###TODO: Create graph
GRAPH_PARAS = {
    "id":"graph-1",
    "name":"Sleep Tracker",
    "unit":"hours",
    "type":"int",
    "color":"sora",
}

HEADERS = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url="https://pixe.la/v1/users/faithisaunicorn/graphs", json=GRAPH_PARAS, headers=HEADERS)

###TODO: Set today's date
result = str(datetime.date.today()) #in YYmmDD format
today = result.replace('-', '')
print(today)

###TODO: Post value to graph
INPUT_PARAS = {
    "date": f"{today}",
    "quantity": input("How many hours did you sleep last night? "),
}

response = requests.post(url="https://pixe.la/v1/users/faithisaunicorn/graphs/graph-1", json=INPUT_PARAS, headers=HEADERS)

###TODO: Delete a pixel
# response = requests.delete(url="https://pixe.la/v1/users/faithisaunicorn/graphs/graph-1/<date>", headers=HEADERS)
