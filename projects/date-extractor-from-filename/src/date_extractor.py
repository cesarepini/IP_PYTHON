from datetime import date
import logging
import re

__version__ = '1.0'

class NoDateFoundError(ValueError):
    pass

logger = logging.getLogger(__name__)

def date_extractor(filename: str) -> list[date]:
    '''
    Extract and validate dates from a filename.

    Args:
        filename: The filename string to search for dates.

    Returns:
        A list of date objects found in the filename.

    Raises:
        NoDateFoundError: If no valid date is found.
    '''
    date_pattern = r'\d{8,}'
    matches = re.findall(date_pattern, filename)
    if not matches:
        logger.info(f'No date found in filename: {filename}')
        raise NoDateFoundError(f'No date found in filename: {filename}')
    date_prefilter_pattern = r'^(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])$'
    plausible_dates = []
    for m in matches:
        for pos in range(len(m) - 7):
            if re.match(date_prefilter_pattern, m[pos:pos+8]):
                plausible_dates.append(m[pos:pos+8])
    if not plausible_dates:
        logger.info(f'No valid date found in filename: {filename}')
        raise NoDateFoundError(f'No valid date found in filename: {filename}')
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
    else:
        logger.info(f'Found at least one valid date in filename: {filename}: {", ".join(str(d) for d in dates)}')
        return dates