#1 
from datetime import datetime, timedelta

# Get current date
current_date = datetime.now()

# Subtract 5 days
new_date = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Date 5 days ago:", new_date.strftime("%Y-%m-%d"))

#2
from datetime import datetime, timedelta

# Get today's date
today = datetime.now()

# Calculate yesterday and tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#3
from datetime import datetime

# Get current datetime
now = datetime.now()

# Remove microseconds
now_without_microseconds = now.replace(microsecond=0)

print("Original datetime:", now)
print("Datetime without microseconds:", now_without_microseconds)

#4
from datetime import datetime

# Define two dates
date1 = datetime(2025, 2, 10, 14, 30, 0)  # Example date
date2 = datetime(2025, 2, 16, 16, 45, 30)  # Example date

# Calculate difference in seconds
difference = abs((date2 - date1).total_seconds())

print("Difference in seconds:", difference)
