import pytest
from Lab2 import find_min_max, calc_average, calc_median_temperature

# Test cases for find_min_max()
def test_find_min_max_normal():
    assert find_min_max([10, 20, 5, 30]) == (5, 30)

def test_find_min_max_single():
    assert find_min_max([25]) == (25, 25)

def test_find_min_max_negative():
    assert find_min_max([-10, -20, -5, -30]) == (-30, -5)

def test_find_min_max_empty():
    assert find_min_max([]) == None  # Assuming None is returned for an empty list

# Test cases for calc_average()
def test_calc_average_normal():
    assert calc_average([10, 20, 30, 40]) == 25.0

def test_calc_average_single():
    assert calc_average([25]) == 25.0

def test_calc_average_negative():
    assert calc_average([-10, -20, -30, -40]) == -25.0

def test_calc_average_empty():
    assert calc_average([]) == None  # Assuming None is returned for an empty list

# Test cases for calc_median_temperature()
def test_calc_median_temperature_odd():
    assert calc_median_temperature([10, 20, 30]) == 20

def test_calc_median_temperature_even():
    assert calc_median_temperature([10, 20, 30, 40]) == 25.0

def test_calc_median_temperature_single():
    assert calc_median_temperature([25]) == 25

def test_calc_median_temperature_empty():
    assert calc_median_temperature([]) == None  # Assuming None is returned for an empty list
