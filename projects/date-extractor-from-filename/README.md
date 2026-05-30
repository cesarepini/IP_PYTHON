Version: 1.0, date: 20260530
This project contains a function that extracts a date from a filename. The date is expected to be in the format YYYYMMDD. The function also validates the extracted date to ensure it is a valid calendar date.

In version 1.0 the functionality is limited to find and validate a plausible 8-digit sequence in a filename, which passed down as a string. The function returns a valid date string if found valid, else it raises a ValueError and exists without returning anything. If no 8-digit sequence is found, the function exits without returning anything.

Sample usage:
python
from date_extractor import date_extractor

date_extractor("example_20231015.txt")