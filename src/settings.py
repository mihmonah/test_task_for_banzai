import operator
import random


CAPS = {
    'platformName': 'Android',
    'platformVersion': '8.0',
    'app': '',
    'appPackage': 'com.Banzai.QATestTask',
    'appActivity': 'com.unity3d.player.UnityPlayerActivity',
    'avd': '',
    'deviceName': 'My device',
    'noReset': True
}
DR_MOBILE = dict(command_executor='http://localhost:4723/wd/hub',
                 desired_capabilities=None)
EPS = 1e-05
OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


def gen_random_float(len_after_point=None):
    div_len = random.randint(1, 6) if not len_after_point else len_after_point
    return float("%.{}f".format(
        div_len) % random.uniform(1, 100.0))
