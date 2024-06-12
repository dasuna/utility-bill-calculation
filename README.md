# Monthly Main Grid and Solar Grid Power Consumption & Cost Calculation

## Project Overview

The aim of this project is to automate the calculation of monthly main grid and solar grid power consumption and cost (utility bill). IoT devices installed at consumer premises will read energy usages and write them to a Google Spreadsheet. Our software will then process this input data from the Google Spreadsheets and calculate important metrics and utility bills.

### Input Data Structure

The typical structure of the Google Spreadsheet containing energy usage data is as follows:

| unixtimestamp | E_day | E_peak | E_offpeak | Max_kVA | E_solar |
|----------------|-------|--------|-----------|---------|---------|
| 1707973078     | 0     | 11     | 0         | 46      | 27      |
| 1707974878     | 0     | 14     | 0         | 46      | 35      |
| 1707976678     | 0     | 34     | 0         | 47      | 45      |
| 1707978478     | 0     | 46     | 0         | 46      | 64      |
| 1707980278     | 0     | 67     | 0         | 46      | 43      |
| 1707982078     | 0     | 0      | 10        | 35      | 0       |
| 1707983878     | 0     | 0      | 14        | 46      | 0       |
| 1707985678     | 0     | 0      | 34        | 46      | 0       |



The spreadsheet contains columns for the Unix timestamp, daily energy usage, peak energy usage, off-peak energy usage, maximum kilovolt-amperes (kVA), and solar energy production.

### Rate Values

Another spreadsheet holds rate values used in the calculation of utility bills. The structure of this spreadsheet is as follows:

| Year | Month | Day Rate | Peak Rate | Off Peak Rate | Max KVA Rate | Fixed Rate | Solar Bill Type | Solar to Grid Rate | Solar to Plant Rate | CO2 Reduction Rate |
|------|-------|----------|-----------|---------------|--------------|------------|-----------------|--------------------|--------------------|--------------------|
| 2022 | Jan   | 37       | 40        | 24            | 1600         | 5000       | Net Accounting  | 34.5               | 37                 | 1                  |
| 2022 | Feb   | 37       | 40        | 24            | 1600         | 5000       | Net Accounting  | 32                 | 37                 | 1                  |
| 2022 | Mar   | 37       | 40        | 24            | 1600         | 5000       | Net Accounting  | 34.5               | 30                 | 1                  |
| 2022 | Apr   | 37       | 40        | 24            | 1600         | 5000       | Net Plus        | 34.5               | 0                  | 1                  |
| 2022 | May   | 37       | 40        | 24            | 1600         | 5000       | Net Accounting  | 34.5               | 37                 | 1                  |
| 2022 | Jun   | 37       | 40        | 24            | 1600         | 5000       | Net Plus        | 34.5               | 0                  | 1                  |
| 2022 | Jul   | 37       | 40        | 24            | 1600         | 5000       | Net Plus        | 34.5               | 0                  | 1                  |
| 2022 | Aug   | 37       | 40        | 24            | 1600         | 5000       | Net Accounting  | 34.5               | 37                 | 1                  |
| 2022 | Sep   | 37       | 40        | 24            | 1600         | 5000       | Net Accounting  | 34.5               | 37                 | 1                  |
| 2022 | Oct   | 37       | 40        | 24            | 1600         | 5000       | Net Accounting  | 37                 | 37                 | 1                  |



The spreadsheet contains columns for the year, month, day rate, peak rate, off-peak rate, max kVA rate, fixed rate, solar bill type, solar to grid rate, solar to plant rate, and CO2 reduction rate.

## Usage

To use this project, follow these steps:

1. Ensure that the energy usage data is being written to the Google Spreadsheet in the specified format.
2. Make sure the rate values spreadsheet is accessible and up to date.
3. Run the software to process the input data and calculate the utility bills.
 

### Running Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository

2. Install dependencies:

pip install -r requirements.txt

3. Start the application:

python main.py

4. Access the application at http://localhost:8080

## Contributing

Contributions to this project are welcome. If you have suggestions for improvements or would like to report a bug, please open an issue or submit a pull request.




