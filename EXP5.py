#pip install pandas
#pip install openpyxl

import pandas as pd
# Replace 'child labour and child marriage data.xlsx' with the path to your Excel file
excel_file_path = ('child labour and child marriage.xlsx')
# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(r"C:\Users\acer\Desktop\Srinivas-09\cm1.xlsx")
# Display the first few rows of the DataFrame
data_types=df.dtypes
last_ten_rows=df.tail(10)
print(df.head())
print(data_types)
print(last_ten_rows)
# Create a new column filled with NaN values
new_column = ['nan'] * len(df)
# Insert the new column in the sixth position (index 5)
df.insert(5, "NewColumnName", new_column)
# Save the updated DataFrame back to theExcel file
df.to_excel(excel_file_path, index=False)
# Display the DataFrame with the new column
print(df.head()) 
