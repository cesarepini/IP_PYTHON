import pytest

from datetime import date

@pytest.fixture(scope='module')
def valid_cases():
    return [
        ('20210930', [date(2021, 9, 30)]),
        ('20210930.pdf', [date(2021, 9, 30)]),
        ('filing_report_20210930.pdf', [date(2021, 9, 30)]),
        ('filing_report_20210930_to_client_20211002.pdf', [date(2021, 9, 30), date(2021, 10, 2)]),
    ]