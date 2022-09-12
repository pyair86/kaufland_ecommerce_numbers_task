import random


class Number:
    @staticmethod
    def create_random_sorted_numbers(
        number_of_files,
        min_file_length,
        max_file_length,
        min_random_number,
        max_random_number,
    ):
        random_numbers = []
        for i in range(number_of_files):
            file_length = random.randint(min_file_length, max_file_length)
            random_numbers.append(
                random.sample(range(min_random_number, max_random_number), file_length)
            )
            random_numbers[-1].sort()
        return random_numbers
