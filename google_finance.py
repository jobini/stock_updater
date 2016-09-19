import csv
from googlefinance import getQuotes
import time

periodicity = int(raw_input("Enter periodicity (in seconds): "))

def exec_script():
    portfolio = ['GOOGL','FB','TATAMOTORS','ASHOKLEY','SBIN','SLT','INDIAVIX','500020','HINDPETRO','HCC']
    fieldnames = ["AppendTime","Index","LastTradeWithCurrency", \
    "LastTradePrice","LastTradeDateTimeLong","StockSymbol","ID"]
    file_name = 'My Portfolio.csv'

    with open(file_name, 'ab') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for company in portfolio:
            Index = getQuotes(company)[0]["Index"]
            LTWC = getQuotes(company)[0]["LastTradeWithCurrency"]
            LTP = getQuotes(company)[0]["LastTradePrice"]
            LTT = getQuotes(company)[0]["LastTradeDateTimeLong"]
            StockSymbol = getQuotes(company)[0]["StockSymbol"]
            ID = getQuotes(company)[0]["ID"]

            writer.writerow({'AppendTime': time.ctime(), 'Index': Index, \
            'LastTradeWithCurrency': LTWC,'LastTradePrice': LTP,\
            'LastTradeDateTimeLong': LTT, \
            'StockSymbol': StockSymbol, 'ID': ID})
        writer.writerow({'AppendTime': " ", 'Index': " ", \
        'LastTradeWithCurrency': " ",'LastTradePrice': " ",\
        'LastTradeDateTimeLong': " ", \
        'StockSymbol': " ", 'ID': " "})

    print "Successfully appended to {0} at {1}".format(file_name, time.ctime())


while True:
    starttime = time.time()
    exec_script()
    time.sleep(periodicity - ((time.time() - starttime) % periodicity))
