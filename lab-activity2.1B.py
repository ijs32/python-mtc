# Go to your main.py file.

# On the first line, ask the user how many days they've been driving for and declare the user input. It's an integer, so cast the string.

# Then calculate the number of years in that set of days.

# Next, convert the remaining days that weren't converted to years into weeks.

# Then, get any remaining days that weren't converted to weeks.

# Print everything out.
import math
input = int(input("Days you have been driving: "))

years = int(input / 365)
years_decimal = (input / 365) - years
weeks = int(52 * years_decimal)
weeks_decimal = (52 * years_decimal) - weeks
days = math.ceil(weeks_decimal * 7)

print(years)
print(weeks)
print(days)
