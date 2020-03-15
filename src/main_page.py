import logging

from src.base_page import BasePage
from src.locators import calc_locators
from src.settings import EPS

logging.basicConfig(level=logging.INFO)


class MainPage(BasePage):
    def __init__(self, driver=None, locator_map=calc_locators):
        super().__init__(driver, locator_map)

    def click_change_sign(self):
        self.click_button("Button Change Sign")

    def click_clear_entry(self):
        self.click_button("Button Clear Entry")

    def click_equals(self):
        self.click_button("Button Equals")

    def click_erase_symbol(self):
        self.click_button("Button Erase Symbol")

    def click_number(self, n=None):
        self.click_button("Button {}".format(n))

    def click_operation(self, operation):
        if operation == '+':
            self.click_button("Button Plus")
        elif operation == '-':
            self.click_button("Button Minus")
        elif operation == '*':
            self.click_button("Button Multiplication")
        elif operation == '/':
            self.click_button("Button Division")

    def input_number(self, num=0):
        for i in str(num):
            self.click_number(i)

    def is_displayed_number_correct(self, exp_result):
        act_result = self.get_text_from("Result Text")[:-2]
        logging.info(
            ">>> Comparing actual '{}' and expected {} "
            "strings on display.".format(act_result, exp_result))
        return act_result == str(exp_result)

    def is_int_result_correct(self, exp_result):
        act_result = int(self.get_text_from("Result Text"))
        logging.info(
            ">>> Comparing actual '{}' and expected {} "
            "numbers for int.".format(act_result, exp_result))
        return act_result == exp_result

    def is_float_result_correct(self, exp_result, eps=EPS):
        act_result = float(self.get_text_from("Result Text"))
        logging.info(
            ">>> Comparing actual '{}' and expected {} numbers for float. "
            "Approximation accuracy is {}".format(act_result, exp_result, eps))
        return act_result - exp_result <= eps
