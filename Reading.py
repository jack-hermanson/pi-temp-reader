from datetime import datetime
from dataclasses import dataclass


@dataclass()
class Reading:
    """
    A simple object containing a temperature, humidity, and the current time.
    """

    temperature: float
    humidity: float
    generated: datetime = datetime.now()

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

    def log(self):
        """
        Print to the console.
        """
        print(f"[{self.generated}] {self.temperature}f, {self.humidity}%")
