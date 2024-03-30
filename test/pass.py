import json

def update_node_positions(json_data):
    # Example logic to convert coordinates to positions
    # This can be replaced with any logic you need
    min_lon = min(lat_lon["longitude"] for lat_lon in json_data["coordinates"].values())
    max_lon = max(lat_lon["longitude"] for lat_lon in json_data["coordinates"].values())
    min_lat = min(lat_lon["latitude"] for lat_lon in json_data["coordinates"].values())
    max_lat = max(lat_lon["latitude"] for lat_lon in json_data["coordinates"].values())

    width = 600  # Width of the area to project the coordinates onto
    height = 400  # Height of the area

    for node, coord in json_data["coordinates"].items():
        # Normalize the coordinates and scale to the drawing area
        x = (coord["longitude"] - min_lon) / (max_lon - min_lon) * width
        y = (coord["latitude"] - min_lat) / (max_lat - min_lat) * height
        # Update the node_positions with new values
        json_data["node_positions"][node] = [int(x), int(height - y)]  # Flip y for graphical representation

def main():
    json_file_path = 'temp.json'
    
    # Load the JSON data from the file
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
    
    # Update the node positions based on the coordinates
    update_node_positions(json_data)
    
    # Write the updated JSON data back to the file
    with open(json_file_path, 'w') as file:
        json.dump(json_data, file, indent=4)

if __name__ == "__main__":
    main()
