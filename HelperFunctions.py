from time import sleep
from Constants import WAIT_TIME
import os


def convert_temp(degrees_celsius: float) -> float:
    return degrees_celsius * (9/5) + 32


def convert_humidity(raw_humidity: float) -> float:
    return raw_humidity * 0.01


def wait() -> None:
    """
    Just hang out for a bit.
    """

    seconds = int(os.getenv(WAIT_TIME))

    print(f"Waiting {seconds} second{'s' if seconds != 1 else ''}...")
    sleep(seconds)

