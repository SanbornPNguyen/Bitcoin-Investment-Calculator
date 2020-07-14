import requests, csv, datetime, decimal
from bs4 import BeautifulSoup

def scrape():
	FIRST_DATE = "20130428"
	YESTERDAY_DATE = generate_day_string()

	URL = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start={}&end={}".format(FIRST_DATE, YESTERDAY_DATE)
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, "html.parser")

	rows = soup.find_all("tr", {"class": "cmc-table-row"})

	build_csv(rows)

def build_csv(rows):
	with open("data.csv", "w", newline="") as file:
		writer = csv.writer(file)
		writer.writerow(["Date", "Open", "High", "Low", "Close", "Volume", "Market Cap"])

		for row in rows:
			row_as_list = list()
			for element in row.find_all("div"):
				try:
					row_as_list.append(int(element.text.replace(",", "")))
				except ValueError:
					try:
						row_as_list.append(decimal.Decimal(element.text.replace(",", "")))
					except:
						row_as_list.append(element.text)

			writer.writerow(row_as_list)

def generate_day_string():
	today = datetime.datetime.now()
	date_str = today.strftime("%Y") + today.strftime("%m") + str(int(today.strftime("%d")) - 1)
	return date_str

scrape()