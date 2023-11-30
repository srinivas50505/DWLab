import pandas as pd
# Replace 'child labour and child marriage data.xlsx' with the path to your Excel file
excel_file_path = 'child labour and child marriage data.xlsx'
# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(r"C:\Users\acer\Desktop\Srinivas-09\cm1.xlsx")
# Assuming the data you want is in the first sheet (you can specify the sheet name or index)
# Extracting the table from the DataFrame
table_data = df.values
# Display the extracted table
print(table_data)
