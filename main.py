import data_fetcher
import data_processor

raw_data = data_fetcher.fetch(symbol="IBM")
normalized_data = data_processor.normalize(raw_data)
moving_average_data = data_processor.moving_average(raw_data, 6) # 6 timestep, 30 min window


print(raw_data)
print(normalized_data[:10])
print(moving_average_data)