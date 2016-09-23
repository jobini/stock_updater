import csv
from googlefinance import getQuotes
import time
import pandas as pd

periodicity = int(raw_input("Enter periodicity (in seconds): "))

df1 = pd.read_csv('companies.csv')
df2 = pd.DataFrame()
df2["StockSymbol"] = df1["Symbol"]
portfolio = df2["StockSymbol"].tolist()

def exec_script():
    fieldnames = ["AppendTime","Index","LastTradePrice","LastTradeDateTimeLong",\
    "StockSymbol","ID"]
    file_name = 'sample_portfolio.csv'

    with open(file_name, 'ab') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for company in portfolio:
            Index = getQuotes(company)[0]["Index"]
            LTP = getQuotes(company)[0]["LastTradePrice"]
            LTT = getQuotes(company)[0]["LastTradeDateTimeLong"]
            StockSymbol = getQuotes(company)[0]["StockSymbol"]
            ID = getQuotes(company)[0]["ID"]

            writer.writerow({'AppendTime': time.ctime(), 'Index': Index,\
            'LastTradePrice': LTP,'LastTradeDateTimeLong': LTT,\
            'StockSymbol': StockSymbol, 'ID': ID})
        writer.writerow({'AppendTime': " ", 'Index': " ",'LastTradePrice': " ",\
        'LastTradeDateTimeLong': " ",'StockSymbol': " ", 'ID': " "})

    print "Successfully appended to {0} at {1}".format(file_name, time.ctime())


while True:
    starttime = time.time()
    exec_script()
    time.sleep(periodicity - ((time.time() - starttime) % periodicity))
