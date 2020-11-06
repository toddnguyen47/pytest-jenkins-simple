import pytest


@pytest.fixture(scope="class")
def add_by_mult():
    import src.add_by_mult
    add_by_mult_obj = src.add_by_mult.AddByMult()
    yield add_by_mult_obj


class TestAddByMult:
    def test_add_zero_zero(self, add_by_mult):
        assert add_by_mult.add(0, 0) == 0

    def test_add_two_three(self, add_by_mult):
        assert add_by_mult.add(2, 3) == 6

    def test_add_zero_one(self, add_by_mult):
        assert add_by_mult.add(0, 1) == 0

    def test_seven_eight(self, add_by_mult):
        assert add_by_mult.add(7, 8) == 56

    def test_neg_two_three(self, add_by_mult):
        assert add_by_mult.add(-2, 3) == -6

    def test_two_neg_three(self, add_by_mult):
        assert add_by_mult.add(2, -3) == -6

    def test_two_ten_zero(self, add_by_mult):
        assert add_by_mult.add(10, 0) == 0

    def test_neg_two_neg_three(self, add_by_mult):
        assert add_by_mult.add(-2, -3) == 6

    def test_get_one_should_return_one(self, add_by_mult):
        assert add_by_mult.get_one() == 1
