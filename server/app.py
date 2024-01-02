# import RPi.GPIO as GPIO
from flask import Flask, request

HEATING_PIN_MAP = {
    "heat-1": 1,
    "heat-2": 2,
    "heat-3": 3,
    "heat-4": 4,
    "heat-5": 5,
    "heat-6": 6,
}

# GPIO.output(23, GPIO.HIGH)
# GPIO.output(23, GPIO.LOW)

app = Flask(__name__)

@app.post("/floor-heating")
def floor_heating():
    data = request.json
    for key in data:
        if not key in HEATING_PIN_MAP:
            print(f"Received invalid heat key: {key}")
            continue

        pin = HEATING_PIN_MAP[key]
        is_on = data[key] == True
        print(pin, ", ", is_on)
        # GPIO.output(pin, GPIO.HIGH if is_on else GPIO.LOW)

    return data
