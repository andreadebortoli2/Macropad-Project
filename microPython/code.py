print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.layers import Layers
from kmk.handlers.sequences import simple_key_sequence


keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()


keyboard.modules.append(encoder_handler)
keyboard.modules.append(MouseKeys())
keyboard.modules.append(Layers())

#keyboard pins
keyboard.col_pins = (board.GP14, board.GP15,) #write the pins used for matrix column
keyboard.row_pins = (board.GP11, board.GP12, board.GP13,) #write the pins used for matrix row
keyboard.diode_orientation = DiodeOrientation.ROW2COL


#rotary encoder pins
encoder_handler.pins = ((board.GP7, board.GP8, board.GP9),) #write the pins of the encoder, in oredr: pin-a, pin-b, pin-button


#macros
screeenshot = simple_key_sequence(
    (
        KC.LWIN(KC.LSFT(KC.S)),
    )
)

macro1 = simple_key_sequence(
    (
        KC.LCTL(no_release=True), 
        KC.LSFT(no_release=True), 
        KC.LALT(no_release=True), 
        KC.MACRO_SLEEP_MS(30),
        KC.F1,
        KC.MACRO_SLEEP_MS(30),
        KC.LALT(no_press=True),
        KC.LSFT(no_press=True),
        KC.LCTL(no_press=True),
    )
)
macro2 = simple_key_sequence(
    (
        KC.LCTL(no_release=True), 
        KC.LSFT(no_release=True), 
        KC.LALT(no_release=True), 
        KC.MACRO_SLEEP_MS(30),
        KC.F2,
        KC.MACRO_SLEEP_MS(30),
        KC.LALT(no_press=True),
        KC.LSFT(no_press=True),
        KC.LCTL(no_press=True),
    )
)
macro3 = simple_key_sequence(
    (
        KC.LCTL(no_release=True), 
        KC.LSFT(no_release=True), 
        KC.LALT(no_release=True), 
        KC.MACRO_SLEEP_MS(30),
        KC.F3,
        KC.MACRO_SLEEP_MS(30),
        KC.LALT(no_press=True),
        KC.LSFT(no_press=True),
        KC.LCTL(no_press=True),
    )
)
macro4 = simple_key_sequence(
    (
        KC.LCTL(no_release=True), 
        KC.LSFT(no_release=True), 
        KC.LALT(no_release=True), 
        KC.MACRO_SLEEP_MS(30),
        KC.F4,
        KC.MACRO_SLEEP_MS(30),
        KC.LALT(no_press=True),
        KC.LSFT(no_press=True),
        KC.LCTL(no_press=True),
    )
)
macro5 = simple_key_sequence(
    (
        KC.LCTL(no_release=True), 
        KC.LSFT(no_release=True), 
        KC.LALT(no_release=True), 
        KC.MACRO_SLEEP_MS(30),
        KC.F5,
        KC.MACRO_SLEEP_MS(30),
        KC.LALT(no_press=True),
        KC.LSFT(no_press=True),
        KC.LCTL(no_press=True),
    )
)
macro6 = simple_key_sequence(
    (
        KC.LCTL(no_release=True), 
        KC.LSFT(no_release=True), 
        KC.LALT(no_release=True), 
        KC.MACRO_SLEEP_MS(30),
        KC.F6,
        KC.MACRO_SLEEP_MS(30),
        KC.LALT(no_press=True),
        KC.LSFT(no_press=True),
        KC.LCTL(no_press=True),
    )
)
macro7 = simple_key_sequence(
    (
        KC.LCTL(no_release=True), 
        KC.LSFT(no_release=True), 
        KC.LALT(no_release=True), 
        KC.MACRO_SLEEP_MS(30),
        KC.F7,
        KC.MACRO_SLEEP_MS(30),
        KC.LALT(no_press=True),
        KC.LSFT(no_press=True),
        KC.LCTL(no_press=True),
    )
)


# Keymap

keyboard.keymap = [
    #layer 0 base
    [
     macro1,         KC.FD(1),
     KC.MB_LMB,     KC.MB_RMB,
     macro2,      screeenshot,
    ],
    #layer 1
    [
     macro3,     KC.FD(0),
     macro4,       macro5,
     macro6,       macro7,   
    ],
]

# Rotary Encoder
encoder_handler.map = [
                        ((KC.MW_DOWN, KC.MW_UP, KC.MB_LMB),),
                        ((KC.LEFT, KC.RIGHT, KC.MB_LMB),),
                    ]

if __name__ == '__main__':
    keyboard.go()