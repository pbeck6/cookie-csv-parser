# Most Active Cookie
## Description

Given a cookie log file in the following format:
```
cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00
```

The command line program will return the most active cookie for date specified.

For example, `$ python most_active_cookie.py cookie_log.csv -d 2018-12-09` will output:
```
AtY0laUfhglK3lC7
```

## Setup and run
- Install Python 3.9 or greater
- From the command line, run the following: `$ python most_active_cookie.py filename.csv -d YYYY-MM-DD` while specifying parameters `filename.csv` and `-d YYYY-MM-DD`

### Unit tests
- From the command line, run the following: `$ python test_csv_parser.py`

# Modules
## CSV Parser
A module to help parse CSV when conventional libraries are unavailable (csv, pandas, etc.)

Contains the CSVParser class which can parse CSV files into an array, strip headers from the result array, and strip the time from timedate entries.

### parse(filename, header)
Parameters: 
- `filename` as string, containing location of CSV file to be parsed 
- `header` as bool, `header=True` will strip header, False will not, default=True 

Returns: `list[list[str]]`

### strip_header(res)
Parameters: 
- `res` as parsed list object to strip of header 

Returns: `None`, array is modified in-place

Notes: `res` param must be list object returned after parsing through `parse` method

### strip_time(res)
Parameters: 
- `res` as parsed list object to strip of time 

Returns: `None`, array is modified in-place

Notes: `res` param must be list object returned after parsing through `parse` method

### tabulate_matches(res, target, key_index)
Parameters: 
- `res` as parsed list object to check for matches
- `target` as string to check against
- `key_index` as integer, representing index of column in parsed array to use as the key
   For example, if parsed array contains entries in format `['some_string', 'another_string', 'desired_key']`, set index to `2`
   NOTE: set to index of `target` string if desiring TOTAL number of occurrences

Returns: `dict` of key-value pairs with keys set by param

Notes: `res` param must be list object returned after parsing through `parse` method
