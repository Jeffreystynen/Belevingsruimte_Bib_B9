import time
import board
import neopixel



def licht(lijst):
    pixels1 = neopixel.NeoPixel(board.MOSI, 55, brightness=0.05)

    order = lijst[0]
    timing_from_databank = lijst[1]
    color_from_databank = lijst[2]
    brightness = lijst[3]

    for i in range(len(color_from_databank)-1):
        kleur = tuple(map(int, color_from_databank[i].replace('(', '').replace(')', '').split(",")))
        print(kleur)
        time.sleep(timing_from_databank[i])
        pixels1.fill(kleur)