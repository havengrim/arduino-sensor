import pyfirmata

comport = 'COM3'  # Change this to your Arduino's COM port
board = pyfirmata.Arduino(comport)

# Define your LEDs (change the pin numbers if needed)
led_1 = board.get_pin('d:8:o')
led_2 = board.get_pin('d:9:o')
led_3 = board.get_pin('d:10:o')
led_4 = board.get_pin('d:11:o')  # Add more if you have more LEDs
led_5 = board.get_pin('d:12:o')

def led(fingerUp):
    # Turn off all LEDs initially
    led_1.write(0)
    led_2.write(0)
    led_3.write(0)
    led_4.write(0)
    led_5.write(0)

    # Count the number of fingers up
    finger_count = sum(fingerUp)

    # Turn on LEDs based on the number of fingers detected
    if finger_count == 1:
        led_1.write(1)  # 1 finger -> LED 1 on
    elif finger_count == 2:
        led_1.write(1)
        led_2.write(1)  # 2 fingers -> LED 1 and 2 on
    elif finger_count == 3:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)  # 3 fingers -> LED 1, 2, and 3 on
    elif finger_count == 4:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)  # 4 fingers -> LED 1, 2, 3, and 4 on
    elif finger_count == 5:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)  # 5 fingers -> all LEDs on
