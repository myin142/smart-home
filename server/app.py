import RPi.GPIO as GPIO
from flask import Flask, request

HEATING_PIN_MAP = {
    "heat-0": 29,
    "heat-1": 31,
    "heat-2": 33,
    "heat-3": 36,
    "heat-4": 35,
    "heat-5": 38,
    "heat-6": 40,
    "heat-7": 37,
}

app = Flask(__name__)

for k in HEATING_PIN_MAP:
    pin = HEATING_PIN_MAP[k]
    GPIO.setup(pin, GPIO.OUT)

@app.post("/floor-heating")
def floor_heating():
    data = request.json
    for key in data:
        if not key in HEATING_PIN_MAP:
            print(f"Received invalid heat key: {key}")
            continue

        pin = HEATING_PIN_MAP[key]
        is_on = data[key] == True
        print(pin, ": ", is_on)
        GPIO.output(pin, GPIO.HIGH if is_on else GPIO.LOW)

    return data
