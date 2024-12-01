# Write a program that reads an integer number of centuries and converts it to years, days, hours, and minutes.

centuries = int(input())

years_in_century = centuries * 100
days_in_year = int(years_in_century * 365.2422)
hours_in_day = days_in_year * 24
minutes_in_hour = hours_in_day * 60

print(f"{centuries} centuries = {years_in_century} years = {days_in_year} days = {hours_in_day} hours = {minutes_in_hour} minutes")


