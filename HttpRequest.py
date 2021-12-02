from dataclasses import dataclass
from Constants import API_KEY
from Reading import Reading
import requests
import os


@dataclass()
class HttpRequest:
    reading: Reading

    headers = {
        "Authentication": os.getenv(API_KEY)
    }

    def post(self):
        if not self.reading:
            raise TypeError("Reading cannot be None")

        requests.post("https://cs370-temp-reader.herokuapp.com/api/measurements",
                      headers=self.headers,
                      data=self.reading.__dict__())
