import pandas as pd
# Replace 'child labour and child marriage data.xlsx' with the path to your Excel file
excel_file_path = 'child labour and child marriage data.xlsx'
# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(r"C:\Users\acer\Desktop\Srinivas-09\cm1.xlsx")
# Check for duplicate rows
duplicate_rows = df[df.duplicated(keep='first')]
if not duplicate_rows.empty:
 print("Duplicate rows found:")
 print(duplicate_rows)
else:
 print("No duplicate rows found.")
# Check for missing data (NaN values)
missing_data = df.isna().sum()
if missing_data.sum() > 0:
 print("\nMissing data (NaN values) by column:")
 print(missing_data)
else:
     print("\nNo missing data (NaN values) found.")
 # Eliminate rows with missing data (NaN values)
     df_clean = df.dropna()
# Check for missing data (NaN values) again
     missing_data = df_clean.isna().sum()
if missing_data.sum() > 0:
 print("\nMissing data (NaN values) by column:")
 print(missing_data)
else:
 print("\nNo missing data (NaN values) found after elimination.")
# Save the cleaned DataFrame to a new Excel file if needed
# df_clean.to_excel('cleaned_data.xlsx', index=False)
# Clean the data by removing line breaks, spaces, and special characters from all columns
def clean_text(text):
 # Remove line breaks and extra spaces
 text = re.sub(r'\s+', ' ', text)
 # Remove special characters
 text = re.sub(r'[^\w\s]', '', text)
 return text
# Apply the cleaning function to all columns in the DataFrame
 df_cleaned = df.applymap(clean_text)
# Check for duplicate rows in the cleaned DataFrame
 duplicate_rows = df_cleaned[df_cleaned.duplicated(keep='first')]
 if not duplicate_rows.empty:
     print("Duplicate rows found in the cleaned data:")
     print(duplicate_rows)
 else:
     print("No duplicate rows found in the cleaned data.")
# Save the cleaned DataFrame to a new Excel file if needed
# df_cleaned.to_excel('cleaned_data.xlsx', index=False)
