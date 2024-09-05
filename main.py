import data_fetcher
import data_processor

raw_data = data_fetcher.fetch(symbol="IBM")
normalized_data = data_processor.normalize(raw_data)
moving_average_data = data_processor.moving_average(raw_data, 6) # 6 timestep, 30 min window
cumulative_average_data = data_processor.cumulative_average(raw_data)
exponential_average_data = data_processor.exponential_moving_average(raw_data, span=6)
bollinger_bands_data = data_processor.bollinger(raw_data, 6)

print("RAW DATA")
print(raw_data)
print("NORMALIZED DATA")
print(normalized_data[:10])
print("MOVING AVERAGE DATA")
print(moving_average_data)
print("CUMULATIVE AVERAGE DATA")
print(cumulative_average_data)
print("EXPONENTIAL AVERAGE DATA")
print(exponential_average_data)
print("BOLLINGER BANDS")
print(bollinger_bands_data)