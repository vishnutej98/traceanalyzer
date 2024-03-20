from time import sleep

fixed_timer: float = 0.0004

name: str = "Tej"

def mainfunc(name):
    if name:
        print(f'Hello {name}!')
        sleep(fixed_timer)
        print(f'Have a nice day {name}!')
    else:
        ... # Do nothing


if __name__ == "__main__":
    mainfunc(name)
