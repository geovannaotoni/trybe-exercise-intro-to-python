from typing import List


def find_average(numbers: List[int]) -> float:
    sum_of_numbers = 0
    for num in numbers:
        sum_of_numbers += num
    return sum_of_numbers / len(numbers)