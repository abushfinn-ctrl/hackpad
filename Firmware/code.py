import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

# ---- Macros ----
macros = Macros()
keyboard.modules.append(macros)

# ---- Push buttons + encoder button 
PINS = (
    board.D0,  # SW1
    board.D28,  # SW2
    board.D4,  # SW3
    board.D29,  # SW4
    board.D6,   # SW5
    board.D2,   # SW6
    board.D1,   # SW7
    board.D7,   # SW8
    board.D3,   # Encoder button
)

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  # pressed = GND
)

# ---- Rotary Encoder ----
encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.D27, board.D26),  # Encoder A, B
)

encoder.map = [
    (KC.VOLD, KC.VOLU),
]

# ---- Keymap
keyboard.keymap = [
    [
        KC.C,              # SW1
        KC.R,              # SW2
        KC.L,              # SW3
        KC.T,              # SW4
        KC.F,              # SW5
        KC.S,              # SW6
        KC.E,              # SW7
        KC.S,              # SW8
        KC.MUTE,           # Encoder button
    ]
]

if __name__ == '__main__':
    keyboard.go()
