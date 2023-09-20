month = int(input("Input the month (e.g. [1-12]):" ))
day = int(input("Input the day:" ))
mon = ("January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December")
if (month == 1 or month == 2 or month == 12):
	season = 'winter'
elif (month == 3 or month == 4 or month == 5): #('April', 'May', 'June'):
	season = 'spring'
elif (month == 6 or month == 7 or month == 8): #('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'autumn'
print(mon[month - 1], ",", day, ".", "Season is ", season)