import pytest
from datetime import date

from src.date_extractor import date_extractor

@pytest.mark.parametrize("filename, expected", [
    ("20210930", date(2021, 9, 30)),
    ("20210930.pdf", date(2021, 9, 30)),
    ("filing_report_20210930.pdf", date(2021, 9, 30)),
])
def test_valid_dates(filename, expected):
    assert date_extractor(filename) == expected

@pytest.mark.parametrize("filename", [
    "2026_05_30_filing_report.pdf",
    "filing_report_20211330.pdf",
    "filing_report_20260229.pdf",
    "filing_report.pdf",
])
def test_invalid_dates(filename):
    with pytest.raises(ValueError):  # not SystemExit
        date_extractor(filename)