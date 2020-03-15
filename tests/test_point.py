from src.main_page import MainPage
from src.settings import gen_random_float


def test_point(driver_setup):
    a = gen_random_float()
    m_page = MainPage(driver_setup)
    m_page.input_number(a)
    assert m_page.is_displayed_number_correct(a)
