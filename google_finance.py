import csv
from googlefinance import getQuotes
import time
import pandas as pd

periodicity = int(raw_input("Enter periodicity (in seconds): "))

df = pd.read_csv('companies.csv')
portfolio = df["Symbol"].tolist()
company_list = df["Name"].tolist()

def exec_script():
    fieldnames = ["AppendTime","Index","LastTradePrice","LastTradeDateTimeLong",\
    "Name","StockSymbol","ID"]
    file_name = 'sample_portfolio.csv'

    with open(file_name, 'ab') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for i,company in enumerate(portfolio):
            Index = getQuotes(company)[0]["Index"]
            LTP = getQuotes(company)[0]["LastTradePrice"]
            LTT = getQuotes(company)[0]["LastTradeDateTimeLong"]
            StockSymbol = getQuotes(company)[0]["StockSymbol"]
            ID = getQuotes(company)[0]["ID"]

            writer.writerow({'AppendTime': time.ctime(), 'Index': Index,\
            'LastTradePrice': LTP,'LastTradeDateTimeLong': LTT,\
            'Name':company_list[i],'StockSymbol': StockSymbol, 'ID': ID})
        writer.writerow({'AppendTime': " ", 'Index': " ",'LastTradePrice': " ",\
        'LastTradeDateTimeLong': " ",'Name': " ",'StockSymbol': " ", 'ID': " "})

    print "Successfully appended to {0} at {1}".format(file_name, time.ctime())


while True:
    starttime = time.time()
    exec_script()
    time.sleep(periodicity - ((time.time() - starttime) % periodicity))
