import os
import pandas as pd

# Load the CSV file
input_file = "msa_employment.csv"  
data = pd.read_csv(input_file)

output_folder = "msa_occ_employment"
os.makedirs(output_folder, exist_ok=True)

# Iterate through each unique OCC_TITLE
for occ_title in data['OCC_TITLE'].unique():
    # Filter rows by the current OCC_TITLE
    filtered_data = data[data['OCC_TITLE'] == occ_title]
    
    # Replace invalid filename characters in OCC_TITLE
    safe_title = ''.join(c if c.isalnum() or c in (' ', '_') else '_' for c in occ_title)
    
    # Save the filtered data to a new CSV file
    output_file = os.path.join(output_folder, f"{safe_title}_employment.csv")
    filtered_data.to_csv(output_file, index=False)
    
    print(f"Saved {output_file}")

print("All files have been created in the msa_occ_employment folder.")
