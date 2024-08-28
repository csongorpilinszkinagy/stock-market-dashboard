import data_fetcher
import data_processor

raw_data = data_fetcher.fetch(symbol="IBM")
normalized_data = data_processor.normalize(raw_data)

print(raw_data)
print(normalized_data[:10])