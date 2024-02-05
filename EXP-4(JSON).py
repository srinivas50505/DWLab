import xml.etree.ElementTree as ET

def read_xml_file(file_path):

    tree = ET.parse(file_path)

    root = tree.getroot()

    return root

file_path =(r"C:\Users\acer\Desktop\Srinivas-09\my_xml_file.xml")

# Replace with the path to your XML file

xml_root = read_xml_file(file_path)

# Now you can access and manipulate the XML data using the 'xml_root' object

# For example, let's print the tag and text of each element in the XML file:

for element in xml_root.iter():

    print(f"Tag: {element.tag}, Text: {element.text}")
