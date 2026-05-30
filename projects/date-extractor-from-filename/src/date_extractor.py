from datetime import date
import re

def extract_date_from_filename(filename: str) -> str:
    match = re.search(r'\d{8}', filename)
    if match:
        return match.group(0)

def validate_date(date_str: str) -> None:
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise ValueError(f'Invalid date: {date_str}.')
    
def date_extractor(filename: str) -> date:
    date_str = extract_date_from_filename(filename)
    if date_str:
        try:
            validate_date(date_str)
            print(f'Found valid date in filename {filename}: {date_str}')
            return date.fromisoformat(date_str)
        except ValueError as e:
            print(e)
            exit(1)
    else:
        print(f'No date found in filename {filename}')
        exit(1)