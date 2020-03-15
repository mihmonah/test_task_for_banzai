from altunityrunner import AltrunUnityDriver, AltUnityAndroidPortForwarding

from appium.webdriver import Remote


class UnityDriver():
    """docstring for UnityDriver"""
    def __init__(self, driver=Remote, **kwargs):
        self.forwarding = AltUnityAndroidPortForwarding()
        self.forwarding.remove_all_forwards()
        self.forwarding.forward_port_device()

        self.appium_driver = driver(**kwargs)
        self.wait_for_alt_unity_server()
        self.unity_driver = AltrunUnityDriver(self.appium_driver, 'android')

    @staticmethod
    def wait_handler(connect):
        file_obj = connect.socket.makefile()
        for line in file_obj:
            if "AltUnity Driver started" in line:
                break
        file_obj.close()
        connect.close()

    def wait_for_alt_unity_server(self):
        device = self.forwarding.get_device()
        device.shell("logcat -c")
        device.shell("logcat -s Unity", handler=self.wait_handler)
