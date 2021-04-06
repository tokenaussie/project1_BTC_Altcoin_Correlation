# Import the pandas and pathlib libraries
def reader(file1, ticker1):

    import pandas as pd
    from pathlib import Path

# Use the Pathlib libary to set the path to the CSV
    csv_path = Path(file1)

# Use the file path to read the CSV into a DataFrame and display a few rows
    eth_df = pd.read_csv(csv_path, parse_dates=True, index_col="Date", infer_datetime_format=True).drop(columns=["Open", "High", "Low", "Vol.", "Change %"])
    eth_df = eth_df.replace(',', '', regex = True).astype('float64')
    eth_df.columns=[ticker1]
    return eth_df[::-1]