import requests
import os

print("Hello World!")
r = requests.get("https://coreyms.com")
print(r.status_code)

