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

def process_csv_files(raw_data_dir):
    dataframes = []
    complete_metadata = None  # Variable to store the metadata

    for file_name in os.listdir(raw_data_dir):
        if file_name.endswith('.CSV'):
            file_path = os.path.join(raw_data_dir, file_name)
            df, metadata = load_csv_file(file_path)
            if df is not None:
                formatted_df = format_data(df)
                dataframes.append(formatted_df)
                
                # Save the metadata only once (assuming it is the same for all files)
                if complete_metadata is None:
                    complete_metadata = metadata

    # Concatenate all DataFrames
    concatenated_df = pd.concat(dataframes, ignore_index=True)
    return concatenated_df, complete_metadata

def save_csv_file(df, processed_data_path, complete_metadata):
    # Save the DataFrame to a temporary CSV file
    temp_file_path = processed_data_path.replace('.csv', '_temp.csv')
    df.to_csv(temp_file_path, sep=';', index=False, encoding='ISO-8859-1')

    # Write the final file with metadata at the top
    with open(processed_data_path, 'w', encoding='ISO-8859-1') as final_file:
        # Write the metadata
        for line in complete_metadata:
            final_file.write(line + '\n')
        
        # Copy the contents of the temporary file (formatted data) into the final file
        with open(temp_file_path, 'r', encoding='ISO-8859-1') as temp_file:
            for line in temp_file:
                final_file.write(line)
    
    # Remove the temporary file
    os.remove(temp_file_path)
    
    print(f"Formatted file with metadata saved at: {processed_data_path}")

# Processing execution
concatenated_df, complete_metadata = process_csv_files(RAW_DATA_DIR)
save_csv_file(concatenated_df, PROCESSED_DATA_PATH, complete_metadata)
