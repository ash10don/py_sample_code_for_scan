import os
import xml.etree.ElementTree as ET

#Hardcoded credentials (Security Flaw: Sensitive Data Exposure)
DB_USERNAME = "admin"
DB_PASSWORD = "password123"

#Unsafe file handling (No validation)
INPUT_FILE = "data.csv"
OUTPUT_FILE = "output.xml"

# Function to read CSV file (No validation or sanitization)
def read_csv(file_path):
    with open(file_path, "r") as file:  #No error handling
        lines = file.readlines()
    return [line.strip().split(",") for line in lines]

#XML Creation without Encoding (Risk of XML Injection)
def create_xml(data):
    root = ET.Element("Records")
    
    for row in data:
        record = ET.SubElement(root, "Record")
        for i, value in enumerate(row):
            field = ET.SubElement(record, f"Field{i}")  
            field.text = value  #No sanitization (XML Injection risk)
    
    tree = ET.ElementTree(root)
    tree.write(OUTPUT_FILE)
    print(f"XML file '{OUTPUT_FILE}' created.")

#Executing script without input validation
if os.path.exists(INPUT_FILE):
    data = read_csv(INPUT_FILE)
    create_xml(data)
else:
    print(f"Error: File {INPUT_FILE} not found!")  #No logging mechanism
