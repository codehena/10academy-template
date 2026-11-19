import pytest
from src.processor import calculate_mean

def test_calculate_mean_valid():
    assert calculate_mean([10.0, 20.0, 30.0]) == 20.0

def test_calculate_mean_empty():
    with pytest.raises(ValueError):
        calculate_mean([])
