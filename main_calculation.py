import numpy as np
import pandas as pd
import datetime
from cal_month_from_unixtime import month_from_unix_timestamp
from read_private_spread_sheets import read_grid_data, read_rate_card_for_year
from write_to_spread_sheet import write_to_spreadsheet

def calculate_ceb_bill(device_reading_sheet_id, device_reding_sheet_name, rate_card_sheet_id):
    #
    df = read_grid_data(device_reading_sheet_id, device_reding_sheet_name)

    upto_date_bill = 0
    #monthly_amount = 0
    #to keep the track of starting raw of a new month
    start_row = 0
    #final_raw_to_write = []

    int_data_point = df.iloc[0, 0]  # Accessing the cell at row index 0 and column index 0

    init_month, _, year = month_from_unix_timestamp(int_data_point)
    #Load rate card data to a DataFrame by filtering corresponding year
    rate_card_df = read_rate_card_for_year(rate_card_sheet_id, year)

    #monthly_bills = {"Month":"Amount"}
    max_kVA = df.iloc[0, 5]

    #print("value and type of max_kVA",max_kVA, type(max_kVA))

    # Create an empty DataFrame to store calculated values
    #columns = ['Variable1', 'Variable2', 'Variable3']
    #result_df = pd.DataFrame(columns=columns)

    variable1 = []
    variable2 = []
    variable3 = []
    variable4 = []
    variable5 = []
    variable6 = []
    variable7 = []
    variable8 = []
    variable9 = []
    variable10 = []

    for index, row in df.iterrows():

        curent_month, month_name, _ = month_from_unix_timestamp(df.iloc[index, 0])
        temp_max_kVA = df.iloc[index, 5]

        #print("value and type of temp_max_kVA",temp_max_kVA, type(temp_max_kVA))

        if temp_max_kVA > max_kVA:
            max_kVA = temp_max_kVA

        if curent_month == init_month:

            columns_to_include = ['Day Rate', 'Peak Rate', 'Off Peak Rate']
            rate_raw = rate_card_df[rate_card_df['Month'] == month_name]
            coefficient_values = rate_raw[columns_to_include]

            columns_to_include = ['E_day', 'E_peak', 'E_offpeak']
            power_consumption_values = df.loc[index, columns_to_include]

            #taking the dot product of coefficient_values and power_consumption_values 
            current_charge = np.dot(coefficient_values, power_consumption_values)
            #print(current_charge)

            upto_date_bill += float(current_charge[0])

            # Check if it's the last row
            if index == len(df) - 1:
                upto_date_bill += float(max_kVA * rate_raw[['Max KVA Rate']].iloc[0]) + float(rate_raw[['Fixed Rate']].iloc[0])
                sum_column_E_day = df.loc[start_row:index, 'E_day'].sum()
                sum_column_E_peak = df.loc[start_row:index, 'E_peak'].sum()
                sum_column_E_off_peak = df.loc[start_row:index, 'E_offpeak'].sum()
                total_ceb_energy = sum_column_E_day + sum_column_E_peak + sum_column_E_off_peak

                date = datetime.datetime(year, init_month, 28)
                # Format the date as a string in the desired format
                date_string = date.strftime('%m/%d/%Y')
                variable1.append(date_string)
                variable2.append(sum_column_E_day)
                variable3.append(sum_column_E_peak)
                variable4.append(sum_column_E_off_peak)
                variable5.append(total_ceb_energy)
                variable6.append(max_kVA)

                variable8.append(upto_date_bill)
            
        else:
            upto_date_bill += float(max_kVA * rate_raw[['Max KVA Rate']].iloc[0]) + float(rate_raw[['Fixed Rate']].iloc[0])
            sum_column_E_day = df.loc[start_row:index-1, 'E_day'].sum()
            sum_column_E_peak = df.loc[start_row:index-1, 'E_peak'].sum()
            sum_column_E_off_peak = df.loc[start_row:index-1, 'E_offpeak'].sum()
            total_ceb_energy = sum_column_E_day + sum_column_E_peak + sum_column_E_off_peak

            #variable1.append(year)
            #prv_month = datetime.date(1900, init_month, 1).strftime('%b')
            #variable2.append(prv_month)
            date = datetime.datetime(year, init_month, 28)
            # Format the date as a string in the desired format
            date_string = date.strftime('%m/%d/%Y')
            variable1.append(date_string)

            variable2.append(sum_column_E_day)
            variable3.append(sum_column_E_peak)
            variable4.append(sum_column_E_off_peak)
            variable5.append(total_ceb_energy)
            variable6.append(max_kVA)
            
            variable8.append(upto_date_bill)
            
            
            init_month = curent_month
            start_row = index
            upto_date_bill = 0
            max_kVA = 0

            columns_to_include = ['Day Rate', 'Peak Rate', 'Off Peak Rate']
            rate_raw = rate_card_df[rate_card_df['Month'] == month_name]
            coefficient_values = rate_raw[columns_to_include]

            columns_to_include = ['E_day', 'E_peak', 'E_offpeak']
            power_consumption_values = df.loc[index, columns_to_include]

            #taking the dot product of coefficient_values and power_consumption_values 
            current_charge = np.dot(coefficient_values, power_consumption_values)

            upto_date_bill += float(current_charge[0])



    # Create the DataFrame
    result_df = pd.DataFrame({
        "Date": variable1,
        "Day E": variable2,
        "Peak E": variable3,
        "Off Peak E": variable4,
        "Total E": variable5,
        "Max KVA": variable6,
        "CEB Bill": variable8
    })

    write_to_spreadsheet(result_df, 1, rate_card_sheet_id)

