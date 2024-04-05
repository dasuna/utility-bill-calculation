import pandas as pd
import datetime
from cal_month_from_unixtime import month_from_unix_timestamp
from read_private_spread_sheets import read_grid_data, read_rate_card_for_year
from write_to_spread_sheet import write_to_spreadsheet

def calculate_solar_bill(device_reading_sheet_id, device_reding_sheet_name, rate_card_sheet_id):
    #
    df = read_grid_data(device_reading_sheet_id, device_reding_sheet_name)
    upto_date_solar_bill = 0

    #to keep the track of starting raw of a new month
    start_row = 0

    int_data_point = df.iloc[0, 0]  # reading solar unixtimestamp starting value

    init_month, _, year = month_from_unix_timestamp(int_data_point)

    print("init month", init_month)
    #Load rate card data to a DataFrame by filtering corresponding year
    rate_card_df = read_rate_card_for_year(rate_card_sheet_id, year)

    variable1 = []
    variable2 = []
    variable3 = []

    for index, row in df.iterrows():

        curent_month, month_name, _ = month_from_unix_timestamp(df.iloc[index, 0])

        if curent_month == init_month:

            columns_to_include = ['Solar Bill Type', 'Solar to Grid Rate', 'Solar to Plant Rate']
            rate_raw = rate_card_df[rate_card_df['Month'] == month_name]

            coefficient_values = rate_raw[columns_to_include]

            columns_to_include = ['E_solar']
            power_consumption = df.loc[index, columns_to_include]

            # Check if it's the last row
            if index == len(df) - 1:

                sum_column_E_solar = df.loc[start_row:index, 'E_solar'].sum()

                total_solar_energy = sum_column_E_solar

                sum_E_day = df.loc[start_row:index, 'E_day'].sum()

                print("2nd rate raw", rate_raw)

                if rate_raw[['Solar Bill Type']].iloc[0].item() == 'Net Plus':
                    upto_date_solar_bill = total_solar_energy * float(rate_raw[['Solar to Grid Rate']].iloc[0])
                elif rate_raw[['Solar Bill Type']].iloc[0].item() == 'Net Accounting':
                    if total_solar_energy > sum_E_day:
                        upto_date_solar_bill = sum_E_day * float(rate_raw[['Solar to Plant Rate']].iloc[0]) + (total_solar_energy - sum_E_day) * float(rate_raw[['Solar to Grid Rate']].iloc[0])
                    else:
                        upto_date_solar_bill = total_solar_energy * float(rate_raw[['Solar to Plant Rate']].iloc[0])
                else:
                    print("wrong solar bill type")

                date = datetime.datetime(year, init_month, 28)
                # Format the date as a string in the desired format
                date_string = date.strftime('%m/%d/%Y')
                variable1.append(date_string)
                variable2.append(sum_column_E_solar)
                variable3.append(upto_date_solar_bill)
    
        else:
            sum_column_E_solar = df.loc[start_row:index-1, 'E_solar'].sum()
            total_solar_energy = sum_column_E_solar

            sum_E_day = df.loc[start_row:index-1, 'E_day'].sum()

            rate_raw = rate_card_df[rate_card_df['Month'] == month_name]

            if rate_raw[['Solar Bill Type']].iloc[0].item() == 'Net Plus':
                upto_date_solar_bill = total_solar_energy * float(rate_raw[['Solar to Grid Rate']].iloc[0])
            elif rate_raw[['Solar Bill Type']].iloc[0].item() == 'Net Accounting':
                if total_solar_energy > sum_E_day:
                    upto_date_solar_bill = sum_E_day * float(rate_raw[['Solar to Plant Rate']].iloc[0]) + (total_solar_energy - sum_E_day) * float(rate_raw[['Solar to Grid Rate']].iloc[0])
                else:
                    upto_date_solar_bill = total_solar_energy * float(rate_raw[['Solar to Plant Rate']].iloc[0])
            else:
                print("wrong solar bill type")

            date = datetime.datetime(year, init_month, 28)
            # Format the date as a string in the desired format
            date_string = date.strftime('%m/%d/%Y')
            variable1.append(date_string)
            variable2.append(sum_column_E_solar)
            variable3.append(upto_date_solar_bill)
                
            init_month = curent_month
            start_row = index
            upto_date_solar_bill = 0

            columns_to_include = ['Solar Bill Type', 'Solar to Grid Rate', 'Solar to Plant Rate']
            rate_raw = rate_card_df[rate_card_df['Month'] == month_name]
            coefficient_values = rate_raw[columns_to_include]

            columns_to_include = ['E_solar']
            power_consumption = df.loc[index, columns_to_include]


    # Create the DataFrame
    result_df = pd.DataFrame({
        "Date": variable1,
        "Solar E": variable2,
        "Solar Bill": variable3
    })

    write_to_spreadsheet(result_df,7, rate_card_sheet_id)


# Example usage
if __name__ == "__main__":
    calculate_solar_bill('1yp3uPnF4KWN7_cZ_-fac79TnNRrYEOse4Xgx3Z6TEuM','2024','1gUDLFq98NZIQJy7AR7TSQV0SHq_0p-7XyS4KlxCJFK4' )
