from what_is_year_now import what_is_year_now
import pytest

import urllib.request
from unittest.mock import patch
from io import StringIO


def test_first_format():
    """
    Формат даты: YYYY-MM-DD
    """
    date = StringIO('{"currentDateTime": "2022-11-15"}')
    exp_year = 2022
    with patch.object(urllib.request, 'urlopen', return_value=date):
        actual_year = what_is_year_now()
        assert exp_year == actual_year


def test_second_format():
    """
    Фрмат даты: DD.MM.YYYY
    """
    date = StringIO('{"currentDateTime": "15.11.2022"}')
    exp_year = 2022
    with patch.object(urllib.request, 'urlopen', return_value=date):
        actual_year = what_is_year_now()
        assert exp_year == actual_year


def test_incorrect_sep():
    """Некорректный разделитель"""
    date = StringIO('{"currentDateTime": "15:11:2022"}')
    with patch.object(urllib.request, "urlopen", return_value=date):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_incorrect_format():
    """Некорректный формат даты."""
    date = StringIO('{"currentDateTime": "5.11.22"}')
    with patch.object(urllib.request, "urlopen", return_value=date):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_invalid_data():
    """На вход подана не дата"""
    date = StringIO('{"currentDateTime": "11novembver?!thisyear"}')
    with patch.object(urllib.request, 'urlopen', return_value=date):
        with pytest.raises(ValueError):
            what_is_year_now()
