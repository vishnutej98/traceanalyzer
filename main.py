# Python3!
from typing import NoReturn
from time import sleep
import versioninfo

def checkThisFunc() -> NoReturn:
    for i in range(1000):
        if i > 1:
            print(f'Hello world! {i} times')
            sleep(0.3)
        else:
            print(f'Hello world! {i} time')
            sleep(0.3)


if __name__ == "__main__":
    print(f"Version: {versioninfo.application_version} | {versioninfo.application_status}\n")
    checkThisFunc()
