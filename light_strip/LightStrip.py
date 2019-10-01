import board
import neopixel

pixel_pin = board.D18

num_pixels = 30

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.15)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,0,255)
off = (0, 0, 0)

class LightStrip():
    @staticmethod
    def clear():
        for led in range(num_pixels):
            pixels[led] = off
        return list(pixels)

    @staticmethod
    def setState(state):
        for led in range(len(state)):
            pixels[led] = state[led]

    @staticmethod
    def clearFirstHalf():
        for led in range(int(num_pixels/2)):
            pixels[led] = off
        return list(pixels)

    @staticmethod
    def clearSecondHalf():
        for led in range(int(num_pixels/2), num_pixels):
            pixels[led] = off
        return list(pixels)

    @staticmethod
    def firstHalfRed():
        for led in range(int(num_pixels/2)):
            pixels[led] = red
        return list(pixels)

    @staticmethod
    def secondHalfRed():
        for led in range(int(num_pixels/2), num_pixels):
            pixels[led] = red
        return list(pixels)

    @staticmethod
    def secondHalfGreen():
        for led in range(int(num_pixels/2), num_pixels):
            pixels[led] = green
        return list(pixels)

    @staticmethod
    def firstHalfGreen():
        for led in range(int(num_pixels/2)):
            pixels[led] = green
        return list(pixels)

    @staticmethod
    def allRed():
        for led in range(num_pixels):
            pixels[led] = red
        return list(pixels)

    @staticmethod
    def allGreen():
        for led in range(num_pixels):
            pixels[led] = green
        return list(pixels)

    @staticmethod
    def allBlue():
        for led in range(num_pixels):
            pixels[led] = blue
