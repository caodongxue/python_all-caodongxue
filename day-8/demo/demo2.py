import requests

response = requests.get("http://www.baidu.com")
response.encoding = "utf-8"

t = response.text

f = open("百度.html", "w+", encoding="utf-8")

f.write(t)
f.close()
