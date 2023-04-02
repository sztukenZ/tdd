import pytest

from basket import Basket, check_item_name_is_number, check_if_num_positive
from main import run_app, app_controller


def test_check_item_name_is_number_returns_false():
    assert not check_item_name_is_number("test")


def test_check_item_name_is_number_returns_true_provided_int():
    assert check_item_name_is_number(12)


def test_check_item_name_is_number_returns_true_provided_int_str():
    assert check_item_name_is_number("12")


def test_check_if_num_positive_returns_number():
    assert check_if_num_positive("352", int) == 352


def test_check_if_num_positive_returns_none():
    assert check_if_num_positive("elo", int) is None

