import datetime

def month_from_unix_timestamp(timestamp):
    # Convert the Unix timestamp to a datetime object
    datetime_obj = datetime.datetime.utcfromtimestamp(timestamp)
    
    # Extract the month from the datetime object
    month_number = datetime_obj.month
    month_name = datetime_obj.strftime("%b")
    year = datetime_obj.year
    
    return month_number, month_name, year

# Example usage
if __name__ == "__main__":
    unix_timestamp = 1690828068  # Example Unix timestamp
    #month_number, _, _ = month_from_unix_timestamp(unix_timestamp)
    month_number, month_name, _ = month_from_unix_timestamp(unix_timestamp)
    print("Unix Timestamp:", unix_timestamp)
    print("Month Number:", month_number)
    print("Month Name:", month_name)
    #print("Year:", year)
