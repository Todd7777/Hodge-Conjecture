"""Tests for hodge/fermat_degrees.py: which Fermat degrees the cited theorems (MMRV Thm 1.1, Cor. 4.1, Prop. 3.2;
Aoki's generation theorem) already settle.  docs/02-known-cases.md section 2.4."""
from hodge import fermat_degrees as FD


def test_q_divisors():
    assert FD.q_divisors(84) == [12, 21, 28]
    assert FD.q_divisors(88) == [44]
    assert FD.q_divisors(420) == [12, 15, 20, 21, 28, 35, 420]
    assert FD.q_divisors(81) == []
    assert FD.q_divisors(97) == []


def test_consistent_with_mmrv_theorem():
    # MMRV Theorem 1.1: every d < 65 except 44, 51, 52
    for d in range(3, 65):
        assert FD.covered(d) == (d not in (44, 51, 52))


def test_open_degrees_up_to_100():
    assert FD.uncovered(100) == [44, 51, 52, 65, 68, 69, 76, 77, 85, 87, 88, 91, 92, 93, 95]
    newly = [d for d in range(65, 101) if FD.covered(d)]
    assert len(newly) == 24 and 84 in newly and 90 in newly and 100 in newly


def test_minimal_open():
    assert FD.minimal_open_q(100) == [44, 51, 52, 65, 68, 69, 76, 77, 85, 87, 91, 92, 93, 95]
    # 420 = 4*3*5*7 is the first element of Q with four P-factors; it is open, so 420 is not covered
    assert 420 in FD.minimal_open_q(420) and not FD.covered(420)
