import pytest
from utils.utils import get_files_in_folder
from sorting.sort_numbers import SortNumbers


@pytest.fixture()
def sort_numbers():
    source_files = get_files_in_folder(extension="txt", path="/app/tests/fixture")
    sort_numbers = SortNumbers(
        number_of_files=len(source_files), source_files=source_files
    )
    return sort_numbers


def test_get_min_number_per_dataset(sort_numbers):
    min_number = sort_numbers.get_min_number_per_dataset(float("inf"))
    assert min_number == -4


def test_execute_sort(sort_numbers):
    sorted_list = sort_numbers.execute_sort(float("inf"))
    assert sorted_list == sorted(sorted_list)
