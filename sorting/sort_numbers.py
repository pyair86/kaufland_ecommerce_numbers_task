from file_handlers.read_file import ReadFile


class SortNumbers:
    def __init__(self, source_files=None):
        self.sorted_numbers = []
        self.source_files = source_files

    def append_one_number_from_each_file(self, current_numbers_to_check_min_number):
        if not self.sorted_numbers:
            for j in range(len(self.source_files)):
                current_numbers_to_check_min_number.append(float(ReadFile.read_line(self.source_files[j])))

    def sort_elements(self):

        """
        The index in current_numbers represents the file number:

        current_numbers = [0,1,2] -> 0 belongs to first file.

        Adds to sorted_numbers the minimum number from current_numbers each iteration.
        Removes from current_numbers the minimum number.
        Adds to current_numbers for previous removed index, new number from file that had the minimum number.
        """

        current_numbers_to_check_min_number = []

        for i in range(len(self.source_files)):

            self.append_one_number_from_each_file(current_numbers_to_check_min_number)

            while self.source_files:

                min_num = min(current_numbers_to_check_min_number)
                index_min_num = current_numbers_to_check_min_number.index(min_num)

                self.sorted_numbers.append(min_num)

                current_numbers_to_check_min_number.pop(index_min_num)

                self.insert_new_number(current_numbers_to_check_min_number, index_min_num)

        return self.sorted_numbers

    def insert_new_number(self, current_numbers_to_check_min_number, index_min_num):

        try:
            current_numbers_to_check_min_number.insert(
                index_min_num,
                float(ReadFile.read_line(self.source_files[index_min_num])),
            )

        # if last line, file doesn't go float
        except ValueError:
            self.source_files[index_min_num].close()
            self.source_files.pop(index_min_num)

    def print_numbers(self):
        print(self.sorted_numbers)
