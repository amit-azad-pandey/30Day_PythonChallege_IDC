import datetime # imports datetime module

# Calculates no. of days between two dates
date1str = input("Enter 1st date in format DD-MM-YYYY")
date1 = datetime.datetime.strptime(date1str, "%d-%m-%Y")

date2str = input("Enter 2nd date in format DD-MM-YYYY")
date2 = datetime.datetime.strptime(date2str, "%d-%m-%Y")

date_diff = abs(date1.date() - date2.date())
num_days = date_diff.days

print(f"There are {num_days} days between {date1.date()} and {date2.date()}")