# Test task for Banzai Games

## Requirements

appium 1.16.0, python 3.7, unity 2018.4.19f1

## Commands to start tests

```
$ appium > /dev/null 2>&1 &
$ ${ANDROID_HOME}/emulator/emulator @<NAME OF EXISTED AVD> > emulator.log &
'''
Or open existed emulator from Android Studio AVD Manager
'''
$ python3 -m venv ./venv
$ source ./venv/bin/activate
$ pip3 install -r requirements.txt
$ py.test -s -v tests/ --html=results.html --self-contained --apk-path=<PATH TO APK> --AVD=<RUNNING AVD>
```

Results will be in `results.html` file.
