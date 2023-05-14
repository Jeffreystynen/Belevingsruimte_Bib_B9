import time
import board
import neopixel



def licht(lijst):
    pixels1 = neopixel.NeoPixel(board.MOSI, 55, brightness=1)

    order = lijst[0]
    timing_from_databank = lijst[1]
    color_from_databank = lijst[2]

    for i in range(len(color_from_databank)):
        kleur = tuple(map(int, color_from_databank[i].split(",")))
        time.sleep(timing_from_databank[i])
        pixels1.fill(kleur)
