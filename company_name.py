import pandas as pd

def find_name(ticker):
	
	df = pd.read_csv('secwiki_tickers.csv')
	
	
	company = ticker
	company = company.upper()

	for i in range(len(df)):
	    test = df["Ticker"][i]
	    if test == company:
		index = i;

	return df["Name"][index]



