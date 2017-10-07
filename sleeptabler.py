from bs4 import BeautifulSoup
import urllib2
import csv
import math
from datetime import datetime
from datetime import timedelta

r = csv.reader(open('sleeplog.csv'))
sleeplines = [l for l in r]

#First, create a row within a new CSV that has every date as a column.
sleepdates = []

for i in range(0, len(sleeplines)):
	if sleeplines[i][0] not in sleepdates:
		sleepdates.append(sleeplines[i][0])

#Second, set up check values.
checkdate = sleepdates[0]
checktime = 0

#print checktime
#print sleeplines[5]

#Third, write the header row into the CSV file.
with open('newsleeplog.csv', 'a') as csvfile:
			sleepwriter = csv.writer(csvfile, delimiter=',')
			sleepwriter.writerow(sleepdates)

#Fourth, some nested loops.
while checktime < 24:
	#clear out the row that we'll be adding to a new CSV.
	currenttimerow = []
	
	#convert "hourly time" into 24-hour time for display in the final product.
	if checktime - math.floor(checktime) == 0:
		timestring = str(int(math.floor(checktime))) + ':00'
	elif checktime - math.floor(checktime) == .25:
		timestring =  str(int(math.floor(checktime))) + ':15'
	elif checktime - math.floor(checktime) == .5:
		timestring = str(int(math.floor(checktime))) + ':30'
	else:
		timestring = str(int(math.floor(checktime)))  + ':45'
	
	#append to the current time row.
	currenttimerow.append(timestring)
	#for loop to check the given time against every date in our dataset.
	for j in range(1,len(sleepdates)):
		#initialize as the baby being awake.
		asleep = 'no'
		#check every record in the dataset.
		for i in range(0,len(sleeplines)):
			#if the date is the date we're currently checking...
			if sleeplines[i][0] == sleepdates[j]:
				#if the checktime is AFTER the asleep time and BEFORE the awake time...
				if float(checktime >= float(sleeplines[i][1])) and checktime <= float(sleeplines[i][2]):
					#change the asleep variable to "yes".
					asleep = 'yes'
		#if the baby is still not asleep, mark it as "A".
		if asleep == 'no':
			currenttimerow.append("A")
		#otherwise, mark it as "S"
		else:
			currenttimerow.append("S")
	#now we add the current time row to the new CSV.
	print currenttimerow
	with open('newsleeplog.csv', 'a') as csvfile:
			sleepwriter = csv.writer(csvfile, delimiter=',')
			sleepwriter.writerow(currenttimerow)
	#increment the checktime by 15 minutes (one-quarter hour), and go to the next time.
	checktime += 0.25
