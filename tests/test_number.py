import pytest
from sorting.random_number import RandomNumber


@pytest.fixture
def sorted_numbers_for_source_files():
    sorted_numbers_for_source_files = RandomNumber.generate(
        number_of_files=10,
        min_file_length=1,
        max_file_length=10,
        min_random_number=1,
        max_random_number=20,
    )

    return sorted_numbers_for_source_files


def test_create_random_sorted_numbers_check_correct_length(
    sorted_numbers_for_source_files,
):
    # number of files
    assert len(sorted_numbers_for_source_files) == 10


def test_create_random_sorted_numbers_check_each_chunk_sorted(
    sorted_numbers_for_source_files,
):
    flag = True
    for chunk in sorted_numbers_for_source_files:
        if chunk != sorted(chunk):
            flag = False
            break
    assert flag
