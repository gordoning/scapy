import requests

params = {"abc":145}
headers = {""}
response = requests.get("http://httpbin.org/cookies",params=params)
print response.status_code
print response.headers
print response.content
print response.json()
print response.cookies
