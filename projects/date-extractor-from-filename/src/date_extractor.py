from datetime import date
import logging
import re

__version__ = '1.0'

class NoDateFoundError(ValueError):
    pass

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

logger = logging.getLogger()

'''
Function for extracting and validating a date from a filename.
The function accepts a filename as a string.
It returns a date object if a valid date is found in the filename.
Otherwhise, it raises a ValueError with an appropriate message.
'''    
def date_extractor(filename: str) -> date | None:
    date_pattern = r'\d{8,}' # looking for a sequence of at least 8 digits
    # extract every sequence of 8 ot more digits
    matches = re.findall(date_pattern, filename)
    if not matches:
        logger.info(f'No date found in filename: {filename}')
        raise NoDateFoundError(f'No date found in filename: {filename}')
    date_prefilter_pattern = r'^(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])$'
    plausible_dates = []
    for m in matches:
        for pos in range(len(m) - 7): # minus 7 because we need the last 8 digits
            if re.match(date_prefilter_pattern, m[pos:pos+8]):
                plausible_dates.append(m[pos:pos+8])
    if not plausible_dates:
        logger.info(f'No valid date found in filename: {filename}')
        raise NoDateFoundError(f'No valid date found in filename: {filename}')
    if len(plausible_dates) > 1:
        dates = []
        for d in plausible_dates:
            try:
                dates.append(
                    date(
                        int(d[:4]),
                        int(d[4:6]),
                        int(d[6:8])
                    )
                    )
            except ValueError as e:
                logger.error(f'Invalid date found in filename {filename}: {d}.')
                continue
        if not dates:
            logger.info(f'No valid date found in filename: {filename}')
            raise NoDateFoundError(f'No valid date found in filename: {filename}')
        if len(dates) > 1:
            logger.info(f'Found multiple valid dates in filename: {filename}, dates: {", ".join(str(d) for d in dates)}')
        else:
            logger.info(f'Found valid date in filename: {filename}, date: {dates[0]}')
            return dates[0]
    else:
        try:
            return date(
                int(plausible_dates[0][:4]),
                int(plausible_dates[0][4:6]),
                int(plausible_dates[0][6:8])
                    )
        except ValueError as e:
            logger.error(f'Invalid date found in filename {filename}: {plausible_dates[0]}. Raised error: ValeError, {e}')
            raise ValueError(f'Invalid date found in filename {filename}: {plausible_dates[0]}. Error: {e}')