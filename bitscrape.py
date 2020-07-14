import requests
from bs4 import BeautifulSoup

URL = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20200713"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

rows = soup.find_all("tr", {"class": "cmc-table-row"})

for row in rows:
	print(row.find_all("div")[0].text)
	for element in row.find_all("div")[1::]:
		print(element.text, end = " ")