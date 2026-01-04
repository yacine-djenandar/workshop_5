import pytest
from src.models.row_2_list import row_to_list

def test_empty_string_returns_empty_list():
    result = row_to_list("")
    assert len(result) == 0

def test_same_length_of_list_as_array():
    example = "12345\t6789s\tdfsdfsdf"
    result = row_to_list(example)
    assert len(result) == len(example.split())
    
