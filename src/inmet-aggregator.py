import pandas as pd
import os

# Paths for the raw data directory and the processed CSV file
RAW_DATA_DIR = 'data/raw/INMET_NE_SE_A421_BREJO GRANDE'
PROCESSED_DATA_PATH = 'data/processed/formatted_data.csv'

def load_csv_file(file_path):
    try:
        # Load the first 8 lines as metadata
        with open(file_path, 'r', encoding='ISO-8859-1') as f:
            metadata = [next(f).strip() for _ in range(8)]  # Capture the first 8 lines

        # Load the CSV, skipping the first 8 metadata lines
        df = pd.read_csv(
            file_path,
            skiprows=8,
            delimiter=';',
            encoding='ISO-8859-1',
            index_col=False
        )
        
        # Remove columns that are completely empty
        df.dropna(how='all', axis=1, inplace=True)
        return df, metadata
    except Exception as e:
        print(f"Error processing the file {file_path}: {e}")
        return None, None

def format_data(df):
    # Rename and format columns
    if 'RADIACAO GLOBAL (KJ/m²)' in df.columns:
        df.rename(columns={
            'RADIACAO GLOBAL (KJ/m²)': 'RADIACAO GLOBAL (Kj/m²)'
        }, inplace=True)
    
    if 'DATA (YYYY-MM-DD)' in df.columns:
        df.rename(columns={
            'DATA (YYYY-MM-DD)': 'Data',
        }, inplace=True)
        
        # Format the date column
        df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d').dt.strftime('%Y/%m/%d')

    if 'HORA (UTC)' in df.columns:
        df.rename(columns={
            'HORA (UTC)': 'Hora UTC',
        }, inplace=True)
        
        # Format the hour column
        df['Hora UTC'] = df['Hora UTC'].apply(lambda x: f"{x.replace(':', '')} UTC")

    return df