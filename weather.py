import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename='sitka_weather_07-2014.csv'
with open(filename) as f: #opens the file
    reader=csv.reader(f) #reads the file
    header_row=next(reader)#it execute the 1st line of the file
   #let us print the column and index to make the objects more meaninigful
    for index,column_header in enumerate(header_row):
        print(index,column_header)
    dates,highs=[],[]
    for row in reader:
        date=datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(date)
       
        high=int(row[1])
        highs.append(high)
        #this prints high temperature, counting as 2nd iteration bt actually indexed as 1
    print(highs)
#plot the data
plt.title("High temperature,july 2014",fontsize=25)
fig=plt.figure(figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.xlabel("day",fontsize=8)
fig.autofmt_xdate() 
# sets date diagonally to prevent overlapping
plt.ylabel("Temperature[F]",fontsize=8)

# sets date diagonally to prevent overlapping
plt.tick_params(axis='both',which='major',labelsize=6)
plt.show()
