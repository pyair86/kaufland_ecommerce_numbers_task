import pytest
from utils.utils import get_files_in_folder
from sorting.sort_numbers import SortNumbers
from file_handlers.open_files import open_files


@pytest.fixture()
def sort_numbers():
    source_files = get_files_in_folder(extension="txt", path="/app/tests/fixture")
    files = open_files(source_files)
    sort_numbers = SortNumbers(files)
    return sort_numbers


def test_execute_sort_check_is_sorted(sort_numbers):
    sorted_list = sort_numbers.sort_elements()
    assert sorted_list == sorted(sorted_list)


def test_execute_sort_check_correct_length(sort_numbers):
    sorted_list = sort_numbers.sort_elements()
    assert len(sorted_list) == 20


def test_execute_sort_check_first_number_is_correct(sort_numbers):
    sorted_list = sort_numbers.sort_elements()
    assert sorted_list[0] == -4


def test_execute_sort_check_last_number_is_correct(sort_numbers):
    sorted_list = sort_numbers.sort_elements()
    assert sorted_list[-1] == 11
