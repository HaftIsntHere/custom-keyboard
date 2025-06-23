import time
import board
import busio
from kmk.kmk.kmk_keyboard import KMKKeyboard
from kmk.kmk.scanners import DiodeOrientation
from kmk.kmk.keys import KC
from kmk.kmk.modules.encoder import EncoderHandler
from kmk.kmk.extensions.display.ssd1306 import SSD1306
from kmk.kmk.extensions.display import Display, TextEntry

keyboard = KMKKeyboard()

i2c_bus = busio.I2C(board.IO16, board.IO15)

driver = SSD1306(
    width=128,
    height=32,
    i2c=i2c_bus,
)

display = Display(
    display=driver,
    width=128,
    height=32,
    brightness=1.0,
    brighness_step=0.1,
)

display.entries = [TextEntry(display, "Welcome!", x=0, y=0)]
keyboard.extensions.append(display)

keyboard.row_pins = (
    board.IO18,
    board.IO21,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
)

keyboard.col_pins = (
    board.IO0,
    board.IO1,
    board.IO2,
    board.IO3,
    board.IO4,
    board.IO5,
    board.IO6,
    board.IO7,
    board.IO8,
    board.IO9,
    board.IO10,
    board.IO11,
    board.IO12,
    board.IO13,
    board.IO14,
    board.IO17,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.ESC,
        KC.F1,
        KC.F2,
        KC.F3,
        KC.F4,
        KC.F5,
        KC.F6,
        KC.F7,
        KC.F8,
        KC.F9,
        KC.F10,
        KC.F11,
        KC.F12,
        KC.NO,
        KC.N0,
        KC.N0,
    ],
    [
        KC.GRAVE,
        KC._1,
        KC._2,
        KC._3,
        KC._4,
        KC._5,
        KC._6,
        KC._7,
        KC._8,
        KC._9,
        KC._0,
        KC.MINS,
        KC.EQL,
        KC.BSPC,
        KC.PGUP,
        KC.N0,
    ],
    [
        KC.TAB,
        KC.Q,
        KC.W,
        KC.E,
        KC.R,
        KC.T,
        KC.Y,
        KC.U,
        KC.I,
        KC.O,
        KC.P,
        KC.LBRC,
        KC.RBRC,
        KC.BSLS,
        KC.PGDN,
        KC.N0,
    ],
    [
        KC.CAPS,
        KC.A,
        KC.S,
        KC.D,
        KC.F,
        KC.G,
        KC.H,
        KC.J,
        KC.K,
        KC.L,
        KC.SCLN,
        KC.QUOT,
        KC.ENT,
        KC.NO,
        KC.HOME,
        KC.N0,
    ],
    [
        KC.LSFT,
        KC.Z,
        KC.X,
        KC.C,
        KC.V,
        KC.B,
        KC.N,
        KC.M,
        KC.COMM,
        KC.DOT,
        KC.SLSH,
        KC.RSFT,
        KC.UP,
        KC.N0,
        KC.END,
        KC.F13,
    ],
    [
        KC.LCTL,
        KC.LALT,
        KC.LGUI,
        KC.N0,
        KC.N0,
        KC.SPC,
        KC.N0,
        KC.N0,
        KC.RGUI,
        KC.FN0,
        KC.RCTL,
        KC.LEFT,
        KC.DOWN,
        KC.N0,
        KC.RIGHT,
        KC.F14,
    ],
]


encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = ((board.IO47, board.IO46, board.IO45),)

encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.MUTE))]


print("Keyboard online!")
