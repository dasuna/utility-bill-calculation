import gspread
import pandas as pd

gc = gspread.service_account('key.json')

def read_google_sheet_to_dataframe(sheet_id, sheet_name):
    spreadsheet = gc.open_by_key(sheet_id)
    worksheet = spreadsheet.worksheet(sheet_name)
    # Specify the expected header row (assuming your header row is unique)
    expected_headers = worksheet.row_values(1)
    rows = worksheet.get_all_records(expected_headers=expected_headers)
    df = pd.DataFrame(rows)
    return df

def read_grid_data(sheet_id, sheet_name):
    #SHEET_ID = '1lo6hrsyTD7qC8zfGwjDwvZEad_gaoys8NS3kObqMpac'
    #SHEET_NAME = '2024'
    SHEET_ID = sheet_id
    SHEET_NAME = sheet_name
    df = read_google_sheet_to_dataframe(SHEET_ID, SHEET_NAME)
    return df

def read_rate_card_for_year(sheet_id, year):
    #SHEET_ID = '1viRbQ3_usatdeywLrPyMIvZZ7i2kd5AjhUNvsvSmVEc'
    #SHEET_NAME = 'Rate Card'
    SHEET_ID = sheet_id
    SHEET_NAME = 'Rate Card'
    df = read_google_sheet_to_dataframe(SHEET_ID, SHEET_NAME)
    # Filter the DataFrame based on the specified year
    filtered_df = df[df["Year"] == year]
    return filtered_df
    #return df

# Example usage
if __name__ == "__main__":
    #filtered_df = read_rate_card_for_year(2017)  # Example
    #print(filtered_df)
    print(read_grid_data())