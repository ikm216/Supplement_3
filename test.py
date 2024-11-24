def convertToFah(cel):
    return (cel * 9/5) + 32

def test_should_return_89point6_from_32():
    assert convertToFah(32) == 89.6
    