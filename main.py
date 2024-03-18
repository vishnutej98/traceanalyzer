# Python3!
from typing import NoReturn
from time import sleep
import versioninfo

set_timer: float = 0.1

def checkThisFunc() -> NoReturn:
    for i in range(100):
        if i > 1:
            print(f'Hello world! {i} times')
            sleep(set_timer)
        else:
            print(f'Hello world! {i} time')
            sleep(set_timer)


if __name__ == "__main__":
    print(f"Version: {versioninfo.application_version} | {versioninfo.application_status}\n")
    checkThisFunc()
