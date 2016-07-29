# this program takes a month (integer between 1 and 12) as a parameter and returns the number of days in that month in a non-leap year (February has 28 days)
# print the days of all 12 months
def daysInMonth(month):
	days = 30
	if (month <= 7):
#needs a less than or equals to because this part is to separate the double 31 months		
		if (month % 2 == 1):
#needs a percent sign so that it involves odds and evens			
			days = 31
		if (month == 2):
#needed another equals sign so that it means if month is 2			
			days = 28
	else:
		if (month % 2 == 0):
#same percent fix as above			
			days = 31
	return days

for i in range(1, 13):
#adjusted range	
	print daysInMonth(i)
