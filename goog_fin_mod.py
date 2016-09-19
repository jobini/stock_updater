import csv
from googlefinance import getQuotes
import time, datetime
import pandas as pd

periodicity = int(raw_input("Enter periodicity (in seconds): "))
portfolio = ['523395', '524348', '523204', '500002', '500410', '533096', \
'500303', '500215', 'AKZOINDIA', '532480', '532309', '532335', '532282', \
'532418', '508869', '500477', '500023', '500820', '505029', '519105', \
'532215', '532977', '500032', '532382', '532134', '532525', '500043', \
'500048', '509480', '500049', '500103', '500547', '532523', '500335', \
'532346', 'BOMDYEING', '531276', '500530', '500074', '532792', '519600', \
'CHEMFALKAL', '523489', '500110', '590001', '532210', '512018', '500830', \
'532902', '532179', '500093', '532180', '526783', '500124', '505200', '531162', \
'500086', '500940', '500033', '523696', '532345', '507815', '532296', '532424', \
'500164', '506480', '523277', '500179', '532281', '500180', '500182', '526899',\
'500104', '500696', '532174', '500116', '532822', '530005', '532544', '532832', \
'532960', '532814', '530965', '532388', 'INFY', '531807', '532851', 'ITC', \
'532532', '532617', '500378', 'JSL', '532286', '532162', '600305', '532926',\
'500165', '532652', '590003', '532747', 'KOTAKBANK', '532901', '534690', \
'500510', '500253', '532998', '531642', 'MARUTI', '532819', '526642', '517140',\
'MRF', '530435', '500790', 'NDTV', '513683', '500304', '532541', '523385', \
'600308', '532944', '532607', '524372', '523574', 'FEL', '500540', '532748', \
'500338', '532387', '532461', '590070', '532826', '500359', '507300', '500330', \
'532712', '500390', '503691', '507315', '500376', '505141', '532638', '532670', \
'523236', 'SIEMENS', '533019', '505192', '500285', '532701', '500112', '532200', \
'532191', '512299', '532872', 'SUNPHARMA', 'SUNTV', 'SUZLON', '532276', '531115',\
'532390', 'TATACOFFEE', '532540', '500408', '500800', '500570', '500400', '500470',\
'532371', '532755', '500850', '500411', '500414', '532375', '500114', '532779',\
'517506', '532343', '532505', '532477', '532478', '511389', '500575', '500238',\
'532300', '505537', 'ZEEMEDIA', '531845', '517164', '532454', 'ZEELEARN', 'MCX', \
'532927', '532778', '533121', '500119', '532483', '526801', 'GOLDBEES', '513377',\
'500325', '532221', '534816', '500483', '533519', '500108', '500312', '532800',\
'530007', '526299', '533229', '517571', '532809', '532939', '500294', \
'532798', '500302']

portfolio1 = portfolio[0:100]
portfolio2 = portfolio[100:200]
portfolio3 = portfolio[200:216]

date = str(datetime.date.today())
date = date.split("-")
date.reverse()
currentdate = date
currentdate = '-'.join(currentdate)
currenttime = str(time.ctime())[11:-8]
file_name = '{0}_{1}.csv'.format(currentdate,currenttime)

with open(file_name, 'ab') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["StockSymbol"])

    for stock in portfolio:
        writer.writerow([stock])

df1 = pd.read_csv("companies.csv")
df2 = pd.read_csv(file_name)
df2["Company"] = df1["Name"]
df2.to_csv(file_name)

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
        new_col = new_col + [LTP_list[i]["LastTradePrice"]]

    print len(new_col)
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
