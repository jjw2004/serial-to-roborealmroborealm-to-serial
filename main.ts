input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showLeds(`
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        `)
    serial.writeLine("hello-roborealm")
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showLeds(`
        . # . # .
        # . # . #
        # . . . #
        . # . # .
        . . # . .
        `)
    serial.writeLine("Test")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showLeds(`
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        `)
    serial.writeLine("Well-Son")
})
serial.onDataReceived(serial.delimiters(Delimiters.Hash), function on_data_received() {
    basic.showIcon(IconNames.Ghost)
})
serial.onDataReceived(serial.delimiters(Delimiters.Fullstop), function on_data_received2() {
    basic.showLeds(`
        # . # . #
        . # # # .
        # # # # #
        . # # # .
        # . # . #
        `)
})
