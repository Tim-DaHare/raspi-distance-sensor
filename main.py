import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

TRIG = 4
ECHO = 18

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GREEN =17
YELLOW =27
RED =22

GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)

# region Functions
def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()
        sig_time = end - start

    return sig_time / 0.000058

def green_light():
    GPIO.output(GREEN,GPIO.HIGH)
    GPIO.output(YELLOW,GPIO.LOW)
    GPIO.output(RED,GPIO.LOW)
    
def yellow_light():
    GPIO.output(GREEN,GPIO.LOW)
    GPIO.output(YELLOW,GPIO.HIGH)
    GPIO.output(RED,GPIO.LOW)
    
def red_light():
    GPIO.output(GREEN,GPIO.LOW)
    GPIO.output(YELLOW,GPIO.LOW)
    GPIO.output(RED,GPIO.HIGH)
# endregion 

while True:
    time.sleep(.05)

    distance = get_distance()
    print('Distance: {} centimeters'.format(distance))

    if distance >= 30:
        green_light()
    elif 30 > distance > 10:
        yellow_light()
    elif distance <= 10:
        red_light()

