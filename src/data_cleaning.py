"""
data_cleaning.py

This script gets messy sales data from raw csv files and cleans the data to 
standardize and verify the data.
"""
import pandas as pd # Importing pandas library as it is optimal to manipulate data

raw_file_path = "data/raw/sales_data_raw.csv" # Loads file and creates dataframe to organize data
df = pd.read_csv(raw_file_path)
print(df.columns)

df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns] # Making all collumn names lowercase and replacing the spaces for _ to standardize

if "product_name" in df.columns: # Striping whitespace as it can cause mistakes when grouping / organizing data
    df["product_name"] = df["product_name"].str.strip()
if "category" in df.columns:
    df["category"] = df["category"].str.strip()

df["price"] = pd.to_numeric(df["price"], errors="coerce") #converts to numeric values
df["qty"] = pd.to_numeric(df["qty"], errors="coerce")

df = df.dropna(subset=["price", "qty"]) #Droping rows with missing values as they are essential for the analysis

df = df[(df["price"] >= 0) & (df["qty"] >= 0)] #Remove any possible negative value as they are usually mistakes

output_file_path = "data/processed/sales_data_clean.csv"
df.to_csv(output_file_path, index=False) #putting clean data into the processed folder

