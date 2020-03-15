import logging


logging.basicConfig(level=logging.INFO)


class BasePage:
    def __init__(self, driver=None, locator_map=None):
        self.dr = driver
        self.lm = locator_map

    def click_button(self, element):
        by_method, locator = self.lm[element]
        logging.info(
            ">>> Clicking on button '{}' which was funded by {}".format(
                locator, by_method))
        self.dr.unity_driver.find_object(by_method, locator).tap()

    def get_text_from(self, element):
        by_method, locator = self.lm[element]
        logging.info(
            ">>> Getting text from element '{}' which was funded by {}".format(
                locator, by_method))
        return self.dr.unity_driver.find_object(by_method, locator).get_text()
