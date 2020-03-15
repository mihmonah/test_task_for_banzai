import pytest
from random import randint

from src.main_page import MainPage
from src.settings import OPS


@pytest.mark.parametrize('operation', ['+', '-', '*', '/'])
def test_int_operations(driver_setup, operation):
    a = randint(0, 100)
    b = randint(0, 100)
    if operation == '/':
        a = a * b
    c = OPS[operation](a, b)
    m_page = MainPage(driver_setup)
    m_page.input_number(a)
    m_page.click_operation(operation)
    m_page.input_number(b)
    m_page.click_equals()
    assert m_page.is_int_result_correct(c)
