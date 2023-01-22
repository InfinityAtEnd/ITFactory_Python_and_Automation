import pytest

from ITFactory_Python.seminar_08.app.func import is_div_3_5, NotIntegerNumberException, only_ints


def test_is_div_3_5_example():
	assert is_div_3_5(25) == 5


@pytest.mark.parametrize("number, expected", [
	(45, 35),
	(10, 5),
	(9, 3),
	(17, None)
])
def test_is_div_3_5(number, expected):
	assert is_div_3_5(number) == expected


@pytest.mark.parametrize("numbers", [
	[1, 3, 4, 8, 5, 3.14, 9],
	['ana'],
	[1 + 2j, 7]
])
def test_only_ints(numbers):
	with pytest.raises(NotIntegerNumberException):
		only_ints(numbers)
