import os
import pytest

from src.settings import CAPS, DR_MOBILE
from src.unity_driver import UnityDriver


defaul_apk_path = '{}/build.apk'.format(os.path.abspath('.'))


def pytest_addoption(parser):
    parser.addoption("--apk-path",
                     default=defaul_apk_path,
                     help="Path to *.apk file.")
    parser.addoption("--avd",
                     default='Pixel_XL_API_27',
                     help="AVD to use for testing.")


def pytest_configure(config):
    apk_path = config.getoption("--apk-path")
    current_avd = config.getoption("--avd")
    CAPS.update(
        app=apk_path,
        avd=current_avd
    )
    DR_MOBILE.update(desired_capabilities=CAPS)


@pytest.fixture(scope='function', autouse=True)
def driver_setup():
    current_driver = UnityDriver(**DR_MOBILE)
    yield current_driver
    current_driver.unity_driver.stop()
    current_driver.appium_driver.quit()
    current_driver.forwarding.remove_all_forwards()
