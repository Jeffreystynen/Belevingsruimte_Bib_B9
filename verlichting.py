import time
import board
import neopixel
import ast


def licht(lijst):
    if len(lijst) < 1:
        print("lijst is leeg")
    else:
        order = lijst[0]
        timing_from_databank = lijst[1]
        color_from_databank = lijst[2]
        brightness = lijst[3]

        for i in range(len(color_from_databank)-1):
            pixels1 = neopixel.NeoPixel(board.MOSI, 55, brightness=brightness[i])
            kleur = ast.literal_eval(color_from_databank[i])
            print("kleur")
            time.sleep(timing_from_databank[i])
            pixels1.fill(kleur)
