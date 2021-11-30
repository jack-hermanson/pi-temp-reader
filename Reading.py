from datetime import datetime


class Reading:
    """
    A simple object containing a temperature, humidity, and the current time.
    """

    temperature: float
    humidity: float
    generated: datetime

    def __init__(
            self,
            temperature: float,
            humidity: float,
    ):
        """
        Constructor.

        :param temperature: The temperature in degrees Fahrenheit read in by the DHT22.
        :param humidity: The humidity (as a percentage) read in by the DHT22.
        """
        self.temperature = temperature
        self.humidity = humidity
        self.generated = datetime.now()

    def __dict__(self):
        """
        Get this data in the form of a dictionary (key/val pairs).
        :return: A dictionary that can be sent in the JSON body.
        """

        return {
            "temperature": self.temperature,
            "humidity": self.humidity,
            "generated": self.generated.utcnow().isoformat()
        }
