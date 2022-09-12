from itertools import islice


class SortNumbers:
    def __init__(self, number_of_files, source_files=None):
        self.source_files_current_reading_indices = [0] * number_of_files
        self.sorted_elements = []
        self.source_files = source_files

    def get_min_number_per_dataset(self, min_number):
        file_number = 0

        for file in self.source_files:
            with open(file) as f:
                for line in islice(
                    f,
                    self.source_files_current_reading_indices[file_number],
                    self.source_files_current_reading_indices[file_number] + 1,
                ):
                    number = float(line.strip())
                    if number < min_number:
                        min_number = number
                    else:
                        continue
            file_number += 1
        return min_number

    def append_to_sorted_elements(self, min_number):
        file_number = 0
        for file in self.source_files:
            with open(file) as f:
                for line in islice(
                    f,
                    self.source_files_current_reading_indices[file_number],
                    self.source_files_current_reading_indices[file_number] + 1,
                ):
                    number = float(line.strip())
                    if number == min_number:
                        self.sorted_elements.append(number)
                        self.source_files_current_reading_indices[file_number] += 1
                    elif number > min_number:
                        continue

            file_number += 1

    def execute_sort(self, min_number):
        while True:
            min_num_per_dataset = self.get_min_number_per_dataset(min_number)
            if self.is_end_of_source_files(min_num_per_dataset):
                break
            self.append_to_sorted_elements(min_num_per_dataset)
        return self.sorted_elements

    @staticmethod
    def is_end_of_source_files(min_num_per_dataset):
        return min_num_per_dataset == float("inf")

    def print_numbers(self):
        print(self.sorted_elements)
