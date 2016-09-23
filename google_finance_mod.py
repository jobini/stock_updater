import csv
from googlefinance import getQuotes
import time, datetime
import pandas as pd

periodicity = int(raw_input("Enter periodicity (in seconds): "))

date = str(datetime.date.today())
date = date.split("-")
date.reverse()
currentdate = date
currentdate = '-'.join(currentdate)
currenttime = str(time.ctime())[11:-8]

file_name = '{0}_{1}.csv'.format(currentdate,currenttime)
attribute = 'LastTradePrice'

with open(file_name, 'ab') as csvfile:
    pass

df1 = pd.read_csv("companies.csv")
df2 = pd.DataFrame()
df2["Company"] = df1["Name"]
df2["StockSymbol"] = df1["Symbol"]
df2.to_csv(file_name)

portfolio = df2["StockSymbol"].tolist()
portfolio1 = portfolio[0:100]
portfolio2 = portfolio[100:200]
portfolio3 = portfolio[200:]

def exec_script():
    with open(file_name,'r') as csvfile:
        data = [item for item in csv.reader(csvfile)]

    LTP_list = getQuotes(portfolio1)
    LTP_list2 = getQuotes(portfolio2)
    LTP_list3 = getQuotes(portfolio3)

    LTP_list.extend(LTP_list2)
    LTP_list.extend(LTP_list3)

    t = time.ctime()
    new_col = [t]
    new_data = []

    for i in range(0,len(LTP_list)):
        new_col = new_col + [LTP_list[i][attribute]]

    for i,row in enumerate(data):
        row.append(new_col[i])
        new_data.append(row)

    with open(file_name,'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(new_data)

    print 'Successfully appended to file "{0}" at {1}'.format(file_name, time.ctime())


while True:
    starttime = time.time()
    exec_script()
    time.sleep(periodicity - ((time.time() - starttime) % periodicity))
