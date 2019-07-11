from examples import unnecessary_math


def test_numbers_3_4():
    assert unnecessary_math.Mathmul(3,4).multiply() == 12
