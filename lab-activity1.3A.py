distance_in_miles = 60
completion_time_in_hours = 3
distance_in_knots = distance_in_miles / 1.15078
distance_in_feet = distance_in_miles * 5280
completion_time_in_seconds = completion_time_in_hours * 3600

mph = distance_in_miles / completion_time_in_hours
knots = distance_in_knots / completion_time_in_hours
feet_per_second = distance_in_feet / completion_time_in_seconds

print("the speed in knots is: ", knots)
print("the speed in miles per hour is: ", mph)
print("the speed in feet per second is: ", feet_per_second)