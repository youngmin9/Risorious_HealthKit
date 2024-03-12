import os
import pandas as pd
import xml.etree.ElementTree as ET
import datetime as dt
import sys

def xml_to_csv(file_path):
    print("Converting XML File to CSV...", end="")
    sys.stdout.flush()

    attribute_list = []
    for event, elem in ET.iterparse(file_path, events=('end',)):
        if elem.tag == 'Record' or elem.tag == 'Workout':  # Assuming these are the tags of interest
            child_attrib = elem.attrib
            for metadata_entry in elem.findall('.//MetadataEntry'):
                child_attrib[metadata_entry.get('key')] = metadata_entry.get('value')
            if 'type' not in child_attrib:
                child_attrib['type'] = elem.tag  # Add 'type' attribute if not present
            attribute_list.append(child_attrib)
            elem.clear()  # Clear the element from memory to avoid excessive memory consumption

    health_df = pd.DataFrame(attribute_list)

    # ... (Rest of the function remains unchanged)

    

def preprocess_to_temp_file(file_path):
    print("Pre-processing and writing to temporary file...", end="")
    sys.stdout.flush()

    temp_file_path = "temp_preprocessed_export.xml"
    with open(file_path, 'r', encoding='utf-8') as infile, open(temp_file_path, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if '<!DOCTYPE' not in line:
                outfile.write(line.replace("\x0b", ""))  # Handle invisible characters here

    print("done!")
    return temp_file_path

def xml_to_csv(file_path):
    print("Converting XML File to CSV...", end="")
    sys.stdout.flush()

    attribute_list = []
    for event, elem in ET.iterparse(file_path, events=('end',)):
        if elem.tag == 'Record' or elem.tag == 'Workout':  # Assuming these are the tags of interest
            child_attrib = elem.attrib
            for metadata_entry in elem.findall('.//MetadataEntry'):
                child_attrib[metadata_entry.get('key')] = metadata_entry.get('value')
            attribute_list.append(child_attrib)
            elem.clear()  # Clear the element from memory to avoid excessive memory consumption

    health_df = pd.DataFrame(attribute_list)

    # Simplify the identifiers in 'type' column for readability
    if 'type' in health_df.columns:
      health_df['type'] = health_df['type'].str.replace('HKQuantityTypeIdentifier|HKCategoryTypeIdentifier', "", regex=True)

    # Reorder columns, if necessary, ensuring essential columns come first
    essential_cols = ['type', 'sourceName', 'value', 'unit', 'startDate', 'endDate', 'creationDate']
    cols_order = essential_cols + [col for col in health_df.columns if col not in essential_cols]
    
    missing_cols = set(essential_cols) - set(health_df.columns)
    for col in missing_cols:
      health_df[col] = None
    
    health_df = health_df[cols_order]

    # Sort by startDate
    health_df.sort_values(by='startDate', ascending=False, inplace=True)

    print("done!")
    return health_df

def save_to_csv(health_df):
    print("Saving CSV file...", end="")
    sys.stdout.flush()

    filename = f"apple_health_export_{dt.datetime.now().strftime('%Y-%m-%d')}.csv"
    health_df.to_csv(filename, index=False)

    print("done!")
    return filename

def remove_temp_file(temp_file_path):
    print("Removing temporary file...", end="")
    os.remove(temp_file_path)
    print("done!")
    
def main():
    file_path = "/content/drive/MyDrive/export_cda.xml"
    temp_file_path = preprocess_to_temp_file(file_path)
    health_df = xml_to_csv(temp_file_path)
    csv_file_path = save_to_csv(health_df)
    print(f"CSV file saved as {csv_file_path}")
    remove_temp_file(temp_file_path)

if __name__ == '__main__':
    main()
