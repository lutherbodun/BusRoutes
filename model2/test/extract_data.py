import csv
import json

# Define the path to the CSV file
csv_file_path = 'Transit Windsor Bus Stops.csv'
# Define the path for the output JSON file
json_file_path = 'temp.json'

# Initialize an empty dictionary for the coordinates
coordinates = {}

# Open the CSV file and read data
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # Initialize a counter
    count = 0
    # Limit the number of records processed to 10
    for row in reader:
        if count < 10:
            # Create a unique name for each bus stop by combining 'ON_STREET' and 'AT_STREET'
            stop_name = f"{row['ON_STREET']} & {row['AT_STREET']}"
            # Remove any leading/trailing whitespace
            stop_name = stop_name.strip()
            coordinates[stop_name] = {
                'longitude': float(row['LONGITUDE']),
                'latitude': float(row['LATITUDE'])
            }
            # Increment the counter
            count += 1
        else:
            break  # Stop reading after 10 records

# Save the extracted coordinates to a JSON file
with open(json_file_path, 'w') as jsonfile:
    json.dump({'coordinates': coordinates}, jsonfile, indent=4)

print("Bus stop coordinates for 10 records have been extracted and saved to JSON.")
