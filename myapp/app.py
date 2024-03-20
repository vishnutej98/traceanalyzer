from time import sleep
import fire

fixed_timer: float = 0.0004

# name: str = "Tej"

def mainfunc(name='Tej'):
    if name:
        print(f'Hello {name}!')
        sleep(fixed_timer)
        print(f'Have a nice day {name}!')
        return f"Hello {name}!"
    else:
        ... # Do nothing


if __name__ == "__main__":
    fire.Fire(mainfunc)
