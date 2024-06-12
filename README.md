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



