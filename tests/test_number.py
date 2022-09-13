import pytest
from sorting.random_number import RandomNumber


@pytest.fixture
def generate():
    sorted_numbers_for_source_files = RandomNumber.generate(
        number_of_files=10,
        min_file_length=1,
        max_file_length=10,
        min_random_number=1,
        max_random_number=20,
    )

    return sorted_numbers_for_source_files


def test_generate_random_numbers_check_correct_length(
    generate,
):
    # number of files
    assert len(generate) == 10


def test_generate_random_numbers_check_each_chunk_sorted(
    generate,
):
    flag = True
    for chunk in generate:
        if chunk != sorted(chunk):
            flag = False
            break
    assert flag
