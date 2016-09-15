# py.test gives the testing functionality
import pytest

import tdd

def test_n_neg():
    assert tdd.n_neg('E') == 1
    assert tdd.n_neg('D') == 1
    assert tdd.n_neg('e') == 1
    assert tdd.n_neg('d') == 1
    assert tdd.n_neg('dede') == 4
    assert tdd.n_neg('DEDE') == 4
    assert tdd.n_neg('ALVPE') == 1
    assert tdd.n_neg('ALVPL') == 0


    # errors
    pytest.raises(RuntimeError, "tdd.n_neg('Z')")
    # assert tdd.n_neg('A*VPL') == 0
    # assert tdd.n_neg('BBBZ') == 0
    # assert tdd.n_neg('AZ') == 0
