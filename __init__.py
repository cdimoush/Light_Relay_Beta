from flask import Flask, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

red_pin = 5
green_pin = 6
blue_pin = 13
ON = 0
OFF = 1  # for some reason relay is backwards, ON or 1 means OFF


GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)  # red pin, controls 1st relay
GPIO.setup(green_pin, GPIO.OUT)  # green pin, controls 4th relay (second relay appears broken)
GPIO.setup(blue_pin, GPIO.OUT)  # blue pin, controls 3rd relay


@app.route('/')
def test():
    print('started on')
    return 'Home Page of 8 channel relay control'


@app.route('/red', methods=['GET', 'POST'])
def red():
    print('turning lights red')
    if request.method == 'POST' or request.method == 'GET':
        GPIO.output(red_pin, ON)
        GPIO.output(green_pin, OFF)
        GPIO.output(blue_pin, OFF)
        print('done')
    return 'red'


@app.route('/green', methods=['GET', 'POST'])
def green():
    print('turning lights green')
    if request.method == 'POST' or request.method == 'GET':
        GPIO.output(red_pin, OFF)
        GPIO.output(green_pin, ON)
        GPIO.output(blue_pin, OFF)
        print('done')
    return 'green'


@app.route('/blue', methods=['GET', 'POST'])
def blue():
    print('turning lights blue')
    if request.method == 'POST' or request.method == 'GET':
        GPIO.output(red_pin, OFF)
        GPIO.output(green_pin, OFF)
        GPIO.output(blue_pin, ON)
        print('done')
    return 'blue'


@app.route('/white', methods=['GET', 'POST'])
def white():
    print('turning lights white')
    if request.method == 'POST' or request.method == 'GET':
        GPIO.output(red_pin, ON)
        GPIO.output(green_pin, ON)
        GPIO.output(blue_pin, ON)
        print('done')
    return 'white'


@app.route('/all_off', methods=['GET', 'POST'])
def all_off():
    print('turning lights off')
    if request.method == 'POST' or request.method == 'GET':
        GPIO.output(red_pin, OFF)
        GPIO.output(green_pin, OFF)
        GPIO.output(blue_pin, OFF)
        print('done')
    return 'off'


@app.route('/emergency_off', methods=['GET', 'POST'])
def emergency_off():
    print('program coming to an emergency stop')
    if request.method == 'POST' or request.method == 'GET':
        GPIO.output(red_pin, OFF)
        GPIO.output(green_pin, OFF)
        GPIO.output(blue_pin, OFF)
        GPIO.cleanup()
        print('GPIO pin have been cleaned')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
