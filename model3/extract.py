import csv
import json

# Define the path to the CSV file
csv_file_path = 'Transit Windsor Bus Stops.csv'
# Define the path for the output JSON file
json_file_path = 'read_from_js.json'

# Initialize an empty dictionary for the coordinates
coordinates = {}

# Initialize a counter
counter = 0

# Open the CSV file and read data
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Increment the counter
        counter += 1
        
        # Generate a unique name for each bus stop by combining 'ON_STREET' and 'AT_STREET'
        stop_name = f"{row['ON_STREET']} & {row['AT_STREET']}".strip()
        coordinates[stop_name] = {
            'longitude': float(row['LONGITUDE']),
            'latitude': float(row['LATITUDE'])
        }
        
        # Stop processing after 4 records
        if counter == 4:
            break

# Save the extracted coordinates to a JSON file
with open(json_file_path, 'w') as jsonfile:
    json.dump({'coordinates': coordinates}, jsonfile, indent=4)

print(f"Bus stop coordinates for the first 4 records have been extracted and saved to {json_file_path}.")
