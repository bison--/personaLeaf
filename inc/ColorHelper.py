import colorsys
from math import floor
# https://www.alanzucconi.com/2016/01/06/colour-interpolation/


class ColorHelper:
    @staticmethod
    def lerp_RGB(start_color, end_color, value):
        '''
        public static Color LerpRGB (Color a, Color b, float t)
        {
            return new Color
            (
                a.r + (b.r - a.r) * t,
                a.g + (b.g - a.g) * t,
                a.b + (b.b - a.b) * t,
                a.a + (b.a - a.a) * t
            );
        }
        '''

        return [
            start_color[0] + (end_color[0] - start_color[0]) * value,
            start_color[1] + (end_color[1] - start_color[1]) * value,
            start_color[2] + (end_color[2] - start_color[2]) * value,
        ]

    @staticmethod
    def rgb_to_hsv(color):
        # input
        (r, g, b) = color

        # normalize
        (r, g, b) = (r / 255, g / 255, b / 255)

        # convert to hsv
        (h, s, v) = colorsys.rgb_to_hsv(r, g, b)

        return [h, s, v]

    @staticmethod
    def lerp_HSV(start_hsv, end_hsv, value):
        # this doesn't work properly!
        H = 0
        S = 1
        V = 2

        h = 0.0
        d = end_hsv[H] - start_hsv[H]

        if start_hsv[H] > end_hsv[H]:
            # Swap(a.h, b.h)
            start_hsv[H], end_hsv[H] = end_hsv[H], start_hsv[H]
            d = -d
            value = 1 - value

        # 180deg
        if d > 0.5:
            start_hsv[H] = start_hsv[H] + 1  # 360deg
            h = (start_hsv[H] + value * (end_hsv[H] - start_hsv[H])) % 1  # 360deg

        # 180deg
        if d <= 0.5:
            h = start_hsv[H] + value + d

        return [
            h,  # H
            start_hsv[S] + value * (end_hsv[S] - start_hsv[S]),  # S
            start_hsv[V] + value * (end_hsv[V] - start_hsv[V]),  # V
        ]

    @staticmethod
    def hsv_to_rgb(hsv):
        as_color = colorsys.hsv_to_rgb(
            hsv[0],
            hsv[1],
            hsv[2]
        )

        return [
            ColorHelper.float_to_byte(as_color[0]),
            ColorHelper.float_to_byte(as_color[1]),
            ColorHelper.float_to_byte(as_color[2])
        ]


    @staticmethod
    def float_to_byte(value):
        #(f >= 1.0 ? 255 : (f <= 0.0 ? 0 : (int)floor(f * 256.0)))
        if value >= 1.0:
            return 255
        elif value <= 0.0:
            return 0
        else:
            return int(floor(value * 256.0))
            '''if calculated > 255:
                return 255
            elif calculated < 0:
                return 0
            else:
                return calculated'''

        # broken on 0!
        #return max(0, min(255, int(floor(value * 256.0))))

    # 0 <= stepNumber <= lastStepNumber
    @staticmethod
    def interpolate(startValue, endValue, stepNumber, lastStepNumber):
        return (endValue - startValue) * stepNumber / lastStepNumber + startValue



