import os
import pandas as pd
import json

# all the paths
geojson_file = "../../tl_2024_us_cbsa/cbsa.geojson"  
input_folder = "../../census/msa_occ_employment"
output_folder = "updated_geojson_files"

# output folder
os.makedirs(output_folder, exist_ok=True)

# Load geoJSON data
with open(geojson_file, 'r') as file:
    geojson_data = json.load(file)

# Here iterating through each csv file in the folder
for csv_file in os.listdir(input_folder):
    if csv_file.endswith(".csv"):
        # Loading the CSV file
        csv_path = os.path.join(input_folder, csv_file)
        employment_data = pd.read_csv(csv_path)

        # Both GEOID and AREA have to be integers
        employment_data['TOT_EMP'] = pd.to_numeric(employment_data['TOT_EMP'], errors='coerce').fillna(0).astype(int)
        employment_data['AREA'] = pd.to_numeric(employment_data['AREA'], errors='coerce').fillna(0).astype(int)

        # Create a dictionary mapping AREA (MSA code) to TOT_EMP
        employment_dict = dict(zip(employment_data['AREA'], employment_data['TOT_EMP']))

        # getting TOT_EMP
        for feature in geojson_data['features']:
            msa_code = feature['properties'].get('GEOID')
            if msa_code is not None and msa_code in employment_dict:
                feature['properties']['TOT_EMP'] = employment_dict[msa_code]
            else:
                feature['properties']['TOT_EMP'] = None  # Default if no match found 
                ### Wrong logic here, why is the geojson format not being correctly identified ?

        # Save the updated GeoJSON
        occupation_name = os.path.splitext(csv_file)[0]
        output_file = os.path.join(output_folder, f"{occupation_name}.geojson")
        with open(output_file, 'w') as outfile:
            json.dump(geojson_data, outfile, indent=2)

        print(f"Saved updated GeoJSON for {occupation_name} to {output_file}")

print("All GeoJSON files have been updated and saved.")