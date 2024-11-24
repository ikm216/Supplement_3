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
    return (fah - 32) * 5/9

def test_should_return_89point6_from_32():
    assert convertToFah(32) == 89.6

def test_should_return_0_from_32():
    assert convertToCel(32) == 0
