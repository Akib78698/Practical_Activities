from datetime import datetime, timezone, timedelta

# Define the IST timezone (UTC+5:30)
ist = timezone(timedelta(hours=5, minutes=30))

# Get the current date and time in IST
current_time = datetime.now(ist)

# Format the date and time
formatted_date = current_time.strftime("%a %b %d %H:%M:%S IST %Y")

# Print the formatted date
print(formatted_date)

