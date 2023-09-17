month = input("Input the month (e.g. [1-12]):" )
day = input("Input the day:" )
if (month == "01" or month == "02" or month == "12"):
	season = 'winter'
elif (month == "03" or month == "04" or month == "05"): #('April', 'May', 'June'):
	season = 'spring'
elif (month == "06" or month == "07" or month == "08"): #('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'autumn'

print(season)