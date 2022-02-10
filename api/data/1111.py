import requests

res = requests.get("http://localhost:8080/woniusales/sell")
print(res.text)