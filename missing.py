import re
import pandas as pd
excel_file_path=r"C:\Users\gokul\Desktop\DW Lab\9.MIssing_eliminate_clean\Child-marriage-database.xlsx"
df=pd.read_excel(excel_file_path)
duplicate_rows=df[df.duplicated(keep="first")]
if not duplicate_rows.empty:
    print("Duplicate rows found")
    print(duplicate_rows)
else:
    print("No Duplicate Rows Found")
Missing_data=df.isna().sum()
if Missing_data.sum()>0:
    print("\n Missing data (Nan Values) by column ")
    print(Missing_data)
else:
    print("\n  No Missing data (Nan Values) found ")
df_clean=df.dropna()
Missing_data=df_clean.isna().sum()
if Missing_data.sum()>0:
    print("\n Missing data (Nan Values) by column ")
    print(Missing_data)
else:
    print("\n  No Missing data (Nan Values) found after elimination ")
def clean_text(text):
    text=re.sub(r"\s+"," ",str(text))
    text=re.sub(r"[^\w\s]"," ",str(text))
    return text 
df_cleaned=df.applymap(clean_text)
duplicate_rows=df_cleaned[df_cleaned.duplicated(keep="first")]
if not duplicate_rows.empty:
    print("Duplicate rows found in the cleaned data ")
    print(duplicate_rows)
else:
    print("No Duplicate Rows Found in Cleaned Data \n")
   

    