import RPi.GPIO as GPIO
from flask import Flask, request

HEATING_PIN_MAP = {
    "heat-0": 5,
    "heat-1": 6,
    "heat-2": 13,
    "heat-3": 16,
    "heat-4": 19,
    "heat-5": 20,
    "heat-6": 21,
    "heat-7": 26,
}

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
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
