from file_handlers.read_file import ReadFile


class SortNumbers:
    def __init__(self, source_files=None):
        self.sorted_numbers = []
        self.source_files = source_files

    def populate_initial_numbers_from_each_file(self,numbers):
        if not self.sorted_numbers:
            for j in range(len(self.source_files)):
                numbers.append(float(ReadFile.read_line(self.source_files[j])))

    def sort_elements(self):

        """
        The index in current_numbers represents the file number:

        current_numbers = [0,1,2] -> 0 belongs to first file.

        Adds to sorted_numbers the minimum number from current_numbers each iteration.
        Removes from current_numbers the minimum number.
        Adds to current_numbers for previous removed index, new number from file that had the minimum number.
        """

        current_numbers = []

        for i in range(len(self.source_files)):

            self.populate_initial_numbers_from_each_file(current_numbers)

            while self.source_files:

                min_num = min(current_numbers)
                index_min_num = current_numbers.index(min_num)
                self.sorted_numbers.append(min_num)

                current_numbers.pop(index_min_num)

                # last line in file
                try:
                    current_numbers.insert(index_min_num, float(ReadFile.read_line(self.source_files[index_min_num])))

                except ValueError:
                    self.source_files[index_min_num].close()
                    self.source_files.pop(index_min_num)
        return self.sorted_numbers

    def print_numbers(self):
        print(self.sorted_numbers)
