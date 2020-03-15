from random import randint

from src.main_page import MainPage


def test_clear_entry(driver_setup):
    a = randint(0, 1000)
    m_page = MainPage(driver_setup)
    m_page.input_number(a)
    m_page.click_clear_entry()
    assert m_page.is_int_result_correct(0)
