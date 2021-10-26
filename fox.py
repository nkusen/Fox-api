import requests
import webbrowser

response = requests.get("https://randomfox.ca/floof")
foxy = response.json()

print(foxy['image'])
webbrowser.open(foxy['image'])