import pandas as pd #imports pandas library as it is optimal for handling data

#Copilot assisted function
#Function that loads data from a csv file
def load_data(file_path):
    "Loads the csv into pandas dataframe"
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded {len(df)} rows from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None

#Copilot assisted function
#Function that standardizes column names and rename them
def clean_column_names(df):
    "Standardizes colummn names and rename them"
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    rename_map = {"prodname": "product_name", "qty": "quantity"}
    df = df.rename(columns=rename_map)
    return df

#Copilot assisted function
#Function that strips whitespace from string columns
def strip_whitespace(df):
    "Strip whitespace from string columns."
    for col in ["product_name", "category"]:
        if col in df.columns:
            df[col] = df[col].str.strip()
    return df

#Copilot assisted function
#Function that converts price and quantity columns to numeric
def convert_numeric(df):
    """Convert price and quantity columns to numeric."""
    for col in ["price", "quantity"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

#Copilot assisted function
#Function that handles missing values by dropping rows with missing values
def handle_missing_values(df):
    "drops rows with missing values"
    if "price" in df.columns and "quantity" in df.columns:
        df = df.dropna(subset=["price", "quantity"])
    return df

#Copilot assisted function
#Function that removes rows with negative prices or quantities
def remove_invalid_rows(df):
    "Remove rows with negative price or quantity"
    if "price" in df.columns and "quantity" in df.columns:
        df = df[(df["price"] >= 0) & (df["quantity"] >= 0)]
    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    if df_raw is not None:
        df_clean = clean_column_names(df_raw)
        df_clean = strip_whitespace(df_clean)
        df_clean = convert_numeric(df_clean)
        df_clean = handle_missing_values(df_clean)
        df_clean = remove_invalid_rows(df_clean)
        df_clean.to_csv(cleaned_path, index=False)
        print("Cleaning complete. First few rows:")
        print(df_clean.head())
