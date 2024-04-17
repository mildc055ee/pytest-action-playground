import pytest

import pytest_action_playground

def test_demo(fashion_mnist):
    (x_train, y_train), (x_test, y_test) = fashion_mnist

    assert len(x_train) == len(y_train)
    assert len(x_test) == len(y_test)


def test_add():
    assert pytest_action_playground.add(1, 2) == 3
