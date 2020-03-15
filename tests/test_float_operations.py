import pytest

from src.main_page import MainPage
from src.settings import gen_random_float, OPS


@pytest.mark.parametrize('operation', ['+', '-', '*', '/'])
def test_float_operations(driver_setup, operation):
    a = gen_random_float()
    b = gen_random_float()
    c = OPS[operation](a, b)
    m_page = MainPage(driver_setup)
    m_page.input_number(a)
    m_page.click_operation(operation)
    m_page.input_number(b)
    m_page.click_equals()
    assert m_page.is_float_result_correct(c)
