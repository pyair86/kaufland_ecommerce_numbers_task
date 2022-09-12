import pytest
from utils.utils import get_files_in_folder


@pytest.fixture
def get_source_files():
    source_files = get_files_in_folder(extension="txt", path="/app/source_files_data")
    return source_files


def test_get_files_in_folder_check_correct_length(get_source_files):
    assert len(get_source_files) == 10


def test_get_files_in_folder_check_all_txt(get_source_files):
    assert all("txt" in file for file in get_source_files)
