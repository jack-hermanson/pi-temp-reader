from Reading import Reading
from dotenv import load_dotenv
from HelperFunctions import wait


load_dotenv()

test = Reading(temperature=75.5, humidity=20.1)
print(test.__dict__())
wait()
test = Reading(temperature=75.5, humidity=20.1)
print(test.__dict__())
