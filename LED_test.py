from blinkstick import blinkstick
import time

bstk = blinkstick.find_first()
num_leds = 16

led_test = False

def run_led_test():
    global led_test

    led_test = True

    colors = [
    (255, 255, 255),  # White
    (255, 0, 0),      # Red
    (0, 255, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 255, 0),    # Yellow
    (255, 0, 255),    # Magenta
    (0, 255, 255),    # Cyan
    (128, 128, 128),  # Gray
    (128, 0, 0),      # Maroon
    (0, 128, 0),      # Green (dark)
    (0, 0, 128),      # Navy
    (128, 128, 0),    # Olive
    (128, 0, 128),    # Purple
    (0, 128, 128),    # Teal
    (64, 64, 64),     # Dark Gray
    (255, 165, 0)     # Orange
]


    while led_test:
        for color in colors:
            if not led_test:
                break
            for i in range(num_leds):
                bstk.set_color(channel=0, index=i, red=color[0], green=color[1], blue=color[2])
            time.sleep(0.3)
        led_test = False

def end_light():
    global led_test

    led_test = True

    colors = [
        (255,255,255),
        (0,0,0)

    ]

    while led_test:
        for color in colors:
            if not led_test:
                break
            for i in range(num_leds):
                bstk.set_color(channel=0, index=i, red=color[0], green=color[1], blue=color[2])
            time.sleep(0.2)
        led_test = False

print("This test will change the color of the LEDs 2 times for each color Check the LED to see if it works propperly")

user_input = input("\n\nReady to start the LED test, type 'y' to start.\n\n")

if user_input =="y":
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nStarting LED test...")
    time.sleep(2)
    for _ in range(3):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTest in progress...")
        run_led_test()

    time.sleep(1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLED test completed")
    for _ in range(2):
        end_light()
    input("\n\nPlease disconnect the LED strip\n\nPress ENTER to close the window")
else:
    print("LED test not executed.")