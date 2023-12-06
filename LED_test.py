from blinkstick import blinkstick
import time
import sys
import traceback

bstk = None
num_leds = 16

def initialize_led():
    global bstk
    bstk = blinkstick.find_first()
    if bstk is None:
        print("Error: LED strip not found. Please connect the LED strip and restart the program.")
        sys.exit(1)

def run_led_test():
    try:
        initialize_led()
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
        
        for _ in range(3):
            for color in colors:
                for i in range(num_leds):
                    bstk.set_color(channel=0, index=i, red=color[0], green=color[1], blue=color[2])
                time.sleep(0.3)

    except Exception as e:
        log_error(e)
        print("An error occurred. The program will now exit.")
        sys.exit(1)

def end_light():
    try:
        initialize_led()
        colors = [
            (255, 255, 255),
            (0, 0, 0)
        ]
        
        for _ in range(2):
            for color in colors:
                for i in range(num_leds):
                    bstk.set_color(channel=0, index=i, red=color[0], green=color[1], blue=color[2])
                time.sleep(0.2)
    
    except Exception as e:
        log_error(e)
        print("An error occurred. The program will now exit.")
        sys.exit(1)

def log_error(exception):
    with open("error_log.txt", "a") as f:
        f.write("Error: {}\n".format(exception))
        traceback.print_exc(file=f)

if __name__ == "__main__":
    print("This test will change the color of the LEDs 2 times for each color. Check the LED to see if it works properly")
    
    user_input = input("\nReady to start the LED test, type 'y' to start.\n")
    
    if user_input.lower() == "y":
        print("\nStarting LED test...")
        time.sleep(2)
        try:
            for _ in range(3):
                print("\nTest in progress...")
                run_led_test()
        
            time.sleep(1)
            print("\nLED test completed")
            for _ in range(2):
                end_light()
        
            input("\nPlease disconnect the LED strip\nPress ENTER to close the window")
        except KeyboardInterrupt:
            print("\nLED test interrupted by user.")
        except Exception as e:
            log_error(e)
            print("An error occurred. The program will now exit.")
    else:
        print("LED test not executed.")