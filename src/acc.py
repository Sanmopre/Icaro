import time
import board
import busio
import adafruit_adxl34x
from gpiozero import AngularServo
import math

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)

while True:
    # Get acceleration values
    x, y, z = accelerometer.acceleration

    # Calculate the angle of tilt (pitch) in the x axis
    pitch = math.atan(x / math.sqrt(y * y + z * z))

    # Calculate the angle of tilt (roll) in the y axis
    roll = math.atan(y / math.sqrt(x * x + z * z))

    # Convert the angles from radians to degrees
    pitch = math.degrees(pitch)
    roll = math.degrees(roll)

    print("Pitch: %f, Roll: %f" % (pitch, roll))
    servo.angle = pitch * 2