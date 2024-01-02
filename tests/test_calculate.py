# Umbenennung der Datei zu test_addiere_zahlen.py

def add_numbers(a, b):
    return a + b

def test_positive_numbers():
    number1 = 5
    number2 = 10
    expected_result = 15

    result = add_numbers(number1, number2)
    assert result == expected_result, f"Failure: {number1} + {number2} should be {expected_result} but the actual result shows {result}"

def test_negative_numbers():
    number1 = -3
    number2 = -7
    expected_result = -10

    result = add_numbers(number1, number2)
    assert result == expected_result, f"Failure: {number1} + {number2} should be {expected_result} but the actual result shows {result}"

def test_mixed_numbers():
    number1 = 8
    number2 = -4
    expected_result = 4

    result = add_numbers(number1, number2)
    assert result == expected_result, f"Failure: {number1} + {number2} should be {expected_result} but the actual result shows {result}"


