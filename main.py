from sorting.number import Number
from file_handlers.write_file import WriteFile
from utils.utils import get_files_in_folder
from sorting.sort_numbers import SortNumbers

if __name__ == "__main__":
    sorted_numbers_for_source_files = Number.create_random_sorted_numbers(
        number_of_files=10,
        min_file_length=1,
        max_file_length=10,
        min_random_number=1,
        max_random_number=20,
    )
    WriteFile(sorted_numbers_for_source_files).prepare_source_files()
    source_files = get_files_in_folder(extension="txt", path="/app/source_files_data")
    sort_numbers = SortNumbers(
        number_of_files=len(source_files), source_files=source_files
    )
    sort_numbers.execute_sort(min_number=float("inf"))
    sort_numbers.print_numbers()
