import pytest
import program.controller

def test_get_index_value_param_found_in_middle():
    lst = ["test", "circle", "main", 1, 1]
    param = "circle"
    assert program.controller.get_param_index_value(lst, param) == 1

def test_get_index_value_param_not_found():
    lst = ["circle", "test", "test"]
    param = "list"
    with pytest.raises(ValueError, match=f"{param} not found in the list."):
        program.controller.get_param_index_value(lst, param)

def test_get_index_value_param_last_element():
    lst = ["test", "right", "test", "circle"]
    param = "circle"
    with pytest.raises(ValueError, match=f"{param} is the last element in the list, no value after it."):
        program.controller.get_param_index_value(lst, param)

def test_get_index_value_param_case_insensitive():
    lst = ["circle", "test", "value"]
    param = "CIRCLE"
    assert program.controller.get_param_index_value(lst, param) == 0

def test_get_index_value_empty_list():
    lst = []
    param = "circle"
    with pytest.raises(ValueError, match=f"{param} not found in the list."):
        program.controller.get_param_index_value(lst, param)

