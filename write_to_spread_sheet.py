import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe

# Replace with your credentials
service_account_file = 'key.json'
scopes = ['https://www.googleapis.com/auth/spreadsheets']

# Authenticate
gc = gspread.service_account(filename=service_account_file, scopes=scopes)

# Open the spreadsheet
#spreadsheet = gc.open_by_key('1viRbQ3_usatdeywLrPyMIvZZ7i2kd5AjhUNvsvSmVEc')
#worksheet = spreadsheet.worksheet('Summary')

#worksheet.clear()

def write_to_spreadsheet(df, start_col_index, sheet_id):
    spreadsheet = gc.open_by_key(sheet_id)
    worksheet = spreadsheet.worksheet('Summary')

    # Get the list of dates from the first column of the spreadsheet
    spreadsheet_dates = worksheet.col_values(1)
    
    # Iterate over the rows of the DataFrame
    for index, row in df.iterrows():
        # Find the index of the corresponding date in the spreadsheet
        date_index = spreadsheet_dates.index(row['Date']) + 1  # Add 1 to convert to 1-based indexing
        
        # Convert the row to a list
        #row_values = row.values.tolist()
        row_values = row.iloc[1:].values.tolist()

        # Get the range where the row will be written
        #start_col_index = start_col_index  # Index of the 8th column (0-based indexing)
        start_cell = f"{chr(ord('A') + start_col_index)}{date_index}"  # Start cell in A1 notation
        end_cell = f"{chr(ord(start_cell[0]) + len(df.columns) - 1)}{date_index}"  # End cell in A1 notation
        range_str = f"{start_cell}:{end_cell}"

        # Write the row to the specified range
        worksheet.update(range_str, [row_values], value_input_option="USER_ENTERED")


# Example usage
if __name__ == "__main__":

    result_df = pd.DataFrame({
        "Date": ["02/28/2024", "03/28/2024", "04/28/2024"],
        "Day E": [10, 20, 30],
        "Peak E": [15, 25, 35],
        "Off Peak E": [5, 15, 25],
        "Total E": [30, 60, 90],
        "Max KVA": [50, 100, 150],
        "CEB Bill": [150, 200, 300]
    })

    write_to_spreadsheet(result_df)