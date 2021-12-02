from dataclasses import dataclass
from Constants import API_KEY
from Reading import Reading
import requests
import os
import sys


@dataclass()
class HttpRequest:
    reading: Reading

    def post(self):
        api_key = os.getenv(API_KEY)
        if not self.reading:
            raise TypeError("Reading cannot be None")

        response = requests.post("https://cs370-temp-reader.herokuapp.com/api/measurements",
                                 headers={
                                     "Authentication": api_key
                                 },
                                 data=self.reading.__dict__())
        error = response.status_code != 200
        if error:
            print(api_key)
            print(response.request.headers)
            print(response.request.body)
