import bitscrape, csv
import pandas as pd

def update():
	bitscrape.scrape()

def calculate_return(buy_amount_dollars, buy_date="Apr 28, 2013", sell_date="Jul 14, 2020"):
	df = pd.read_csv("data.csv")

	buy_high =  float(df.loc[df['Date'] == buy_date]["High"])
	buy_low = float(df.loc[df['Date'] == buy_date]["Low"])
	buy_mean = (buy_high + buy_low) / 2

	sell_high = float(df.loc[df['Date'] == sell_date]["High"])
	sell_low = float(df.loc[df['Date'] == sell_date]["Low"])
	sell_mean = (sell_high + sell_low) / 2

	return round(sell_mean * (buy_amount_dollars / buy_mean), 2)