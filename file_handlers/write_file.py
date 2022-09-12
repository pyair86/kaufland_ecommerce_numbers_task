class WriteFile:
    def __init__(self, numbers_per_file):
        self.numbers_per_file = numbers_per_file

    def prepare_source_files(self):

        for file_number in range(len(self.numbers_per_file)):

            file_number_output_name = file_number + 1
            filename = f"source_files_data/file{str(file_number_output_name)}.txt"
            self.prepare_write(filename, file_number)

    def prepare_write(self, filename, file_number):
        with open(filename, "w") as output_file:

            for current_line_index, number in enumerate(
                self.numbers_per_file[file_number]
            ):

                last_line_index = len(self.numbers_per_file[file_number]) - 1

                self.write(current_line_index, last_line_index, output_file, number)

    def write(self, current_line_index, last_line_index, output_file, number):
        if self.is_last_line(current_line_index, last_line_index):
            output_file.write(str(number))
        else:
            output_file.write(str(number) + "\n")

    @staticmethod
    def is_last_line(current_line_index, last_line_index):
        return current_line_index == last_line_index
