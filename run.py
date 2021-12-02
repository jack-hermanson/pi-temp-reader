from sys import stderr
import HelperFunctions
from HttpRequest import HttpRequest
from Reading import Reading
from dotenv import load_dotenv
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

load_dotenv()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    temperature = HelperFunctions.convert_temp(temperature)
    humidity = HelperFunctions.convert_humidity(humidity)

    if humidity is not None and temperature is not None:
        reading = Reading(temperature=temperature,
                          humidity=humidity)
        reading.log()

        request = HttpRequest(reading)
        request.post()

        HelperFunctions.wait()
    else:
        print("Measurement failed", file=stderr)
