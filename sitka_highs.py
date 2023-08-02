from pathlib import Path
import csv
path = Path('sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high temperatures.
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

print(highs)

for index, column_header in enumerate(header_row):
    print(index, column_header)
print(header_row)