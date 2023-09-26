import pandas as pd
from datetime import datetime
import pytz  # Import the pytz library for time zone conversion

# Read the original CSV file
input_file = 'gluchost.entries.csv'
data = pd.read_csv(input_file)

# Convert the UNIX milliseconds timestamp to a datetime object in a specific time zone
# Replace 'America/New_York' with the desired time zone
desired_timezone = pytz.timezone('America/Los_Angeles')
data['datetime'] = pd.to_datetime(data['date'], unit='ms', utc=True).dt.tz_convert(desired_timezone)

# Determine whether each datetime falls on a weekday or weekend
data['day_type'] = data['datetime'].apply(lambda x: 'weekday' if x.weekday() < 5 else 'weekend')

# Split data into separate DataFrames for weekdays and weekends
weekdays_data = data[data['day_type'] == 'weekday']
weekends_data = data[data['day_type'] == 'weekend']

# Define output file names
weekdays_output_file = 'weekdays.csv'
weekends_output_file = 'weekends.csv'

# Write data to separate CSV files for weekdays and weekends
weekdays_data.to_csv(weekdays_output_file, index=False)
weekends_data.to_csv(weekends_output_file, index=False)

print(f'Data has been split and saved to {weekdays_output_file} and {weekends_output_file}.')

