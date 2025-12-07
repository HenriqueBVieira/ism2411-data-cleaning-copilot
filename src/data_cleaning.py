"""
data_cleaning.py

This script gets messy sales data from raw csv files and cleans the data to 
standardize and verify the data.
"""
#Copilot assisted function
#Function that loads data: loads the csv file into a pandas dataframe
def load_data(file_path):
    import pandas as pd
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded {len(df)} rows from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None
import pandas as pd # Importing pandas library as it is optimal to manipulate data

df = load_data("data/raw/sales_data_raw.csv")
if df is None:
    exit()  #stops running if file is missing

#Copilot assisted function
#Function that cleans column names: standardizes column names by making them lowercase and replacing spaces with _
def clean_column_names(df):
    # Clean all column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    # Rename specific columns for clarity
    rename_map = {
        "prodname": "product_name",
        "qty": "quantity"
    }
    df = df.rename(columns=rename_map)
    
    return df

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

