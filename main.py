from sorting.random_number import RandomNumber
from file_handlers.write_file import WriteFile
from file_handlers.open_files import open_files
from utils.utils import get_files_in_folder
from sorting.sort_numbers import SortNumbers

# gets files in folder

if __name__ == "__main__":
    sorted_numbers_for_source_files = RandomNumber.generate(
        number_of_files=10,
        min_file_length=1,
        max_file_length=10,
        min_random_number=1,
        max_random_number=20,
    )
    WriteFile(sorted_numbers_for_source_files).prepare_source_files()
    source_files = get_files_in_folder(extension="txt", path="/app/source_files_data")
    files = open_files(source_files)
    sort_numbers = SortNumbers(files)
    sort_numbers.sort_elements()
    sort_numbers.print_numbers()
