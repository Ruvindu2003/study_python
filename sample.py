import pandas as pd
import matplotlib.pyplot as plt

# Load hourly temperature data and compute daily min/max for the last 7 days
data_path = 'data/temperature_data.csv'

# Read only the first two columns (date, temperature_C) since the file has a duplicate 'date' header
df_raw = pd.read_csv(
	data_path,
	usecols=[0, 1],
	header=0,
	names=['date', 'temperature_C'],
	parse_dates=['date']
)

# Resample to daily granularity and compute min/max
daily = (
	df_raw.set_index('date')
		  .resample('D')['temperature_C']
		  .agg(['max', 'min'])
		  .reset_index()
)

# Keep the last 7 days if available
df = daily.tail(7)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()