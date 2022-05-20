from pytest import fixture


@pytest.fixture
def my_nums():
    return (1, 4, 8, 23, 57, 90)


def add_nums(nums):
    total = 0
    for n in nums:
        total += n
    return total


def test_add_positive_integers(my_nums):
    assert add_nums(my_nums) == 100
