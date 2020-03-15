import pytest
from random import randint
from src.main_page import MainPage


@pytest.mark.parametrize('num_len', ['long', 'short'])
def test_erase_symbol(driver_setup, num_len):
    if num_len == 'long':
        a = randint(10, 10000)
    elif num_len == 'short':
        a = randint(1, 9)
    m_page = MainPage(driver_setup)
    m_page.input_number(a)
    m_page.click_erase_symbol()
    if num_len == 'long':
        assert m_page.is_int_result_correct(int(str(a)[:-1]))
    elif num_len == 'short':
        assert m_page.is_int_result_correct(0)
