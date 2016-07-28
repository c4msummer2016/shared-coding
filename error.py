# this program takes a month (integer between 1 and 12) as a parameter and returns the number of days in that month in a non-leap year (February has 28 days)
# print the days of all 12 months
def daysInMonth(month):
	days = 30
	if (month < 7):
		if (month / 2 == 1):
			days = 31
		if (month *=* 2):
			days = 28
	else:
		if (month / 2 == 0):
			days = 31
	return days

for i in range(12):
	print daysInMonth(i)
