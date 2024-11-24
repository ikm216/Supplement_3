def convertToFah(cel):
    """
    Convert celsius to fahrenheit

    Args:
        cel: The celsius that being converted

    Returns:
        The final result of celsius being converted to fahrenheit
    """
    return (cel * 9/5) + 32

def convertToCel(fah):
     """
    Convert fahrenheit to celsius

    Args:
        fah: The fahrenheit that being converted

    Returns:
        The final result of fahrenheit being converted to celsius
    """
     return (fah - 32) * 5/9

def even(num):
    """
    Checks if a number is even

    Args:
        num: The number that being check if it is even

    Returns:
        A boolean that shows true if even, false if its odd
    """
    return num % 2 == 0

def test_should_return_89point6_from_32():
    assert convertToFah(32) == 89.6

def test_should_return_0_from_32():
    assert convertToCel(32) == 0

def test_should_return_even_from_2():
    assert even(2) is True