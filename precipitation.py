import csv
from datetime import datetime
from matplotlib import pyplot as plt



filename = 'KNYC.csv'
with open(filename) as f:
    reader = csv.reader(f)
    next(reader)
    f.seek(1)

   
    
    #for index, column_header in enumerate(header_row):
        #print(index, column_header)
        
    dates,actuals, averages, records = [],[],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%m/%d/%Y")
            actual=float(row[10])
            average=float(row[11])
            record=float(row[12])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            actuals.append(actual)
            averages.append(average)
            records.append(record)

fig=plt.figure(dpi=128,figsize=(7,4))
plt.plot(dates, actuals, c='blue', alpha=0.5, label="Actual Precipitation")
plt.plot(dates, averages, c='green', alpha= 0.5, label="Average Precipitation")
plt.plot(dates, records, c='red', alpha=0.5, label="Record Precipitation")

plt.legend(loc="upper left")
plt.margins(x=0)

plt.title("NYC Precipitation - July 2014 to July 2015", fontsize=16)
plt.ylabel("Precipitation (\")")
plt.xlabel(' ', fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=12)
            
