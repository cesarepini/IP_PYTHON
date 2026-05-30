from datetime import date
import pytest
from src.date_extractor import date_extractor

# Test cases for date_extractor function, version 1.0
def test_date_extractor():
    assert date_extractor('20210930') == date(2021, 9, 30)
    assert date_extractor('20210930.pdf') == date(2021, 9, 30)
    assert date_extractor('filing_report_20210930.pdf') == date(2021, 9, 30)
    assert date_extractor('20210930_filing_report.pdf') == date(2021, 9, 30)
    assert date_extractor('application_20210930_filing_report.pdf') == date(2021, 9, 30)
    assert date_extractor('20240228.pdf') == date(2024, 2, 28)
    with pytest.raises(SystemExit):
        date_extractor('2026_05_30_filing_report.pdf')
    with pytest.raises(SystemExit):
        date_extractor('filing_report_20211330.pdf')
    with pytest.raises(SystemExit):
        date_extractor('filing_report_20260229.pdf')
    with pytest.raises(SystemExit):
        date_extractor('filing_report.pdf')