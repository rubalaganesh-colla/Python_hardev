def calculate_product(numbers):
    """
    Calculate the product of all numbers in a given tuple.
    :param numbers: Tuple of numbers
    :return: Product of all numbers
    """
    if not isinstance(numbers, tuple):
        raise TypeError("Input must be a tuple.")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the tuple must be integers or floats.")
    product = 1
    for num in numbers:
        product *= num
    return product
if __name__ == "__main__":
    numbers_tuple = (2, 3, 4, 5)
    try:
        result = calculate_product(numbers_tuple)
        print(f"The product of the numbers in the tuple {numbers_tuple} is: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
