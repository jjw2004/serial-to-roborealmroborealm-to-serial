def on_button_pressed_a():
    basic.show_leds("""
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        """)
    serial.write_line("hello-roborealm")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        . # . # .
        # . # . #
        # . . . #
        . # . # .
        . . # . .
        """)
    serial.write_line("Test")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        """)
    serial.write_line("Well-Son")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_data_received():
    basic.show_icon(IconNames.GHOST)
serial.on_data_received(serial.delimiters(Delimiters.HASH), on_data_received)

def on_data_received2():
    basic.show_leds("""
        # . # . #
        . # # # .
        # # # # #
        . # # # .
        # . # . #
        """)
serial.on_data_received(serial.delimiters(Delimiters.FULLSTOP), on_data_received2)
