def def_color(): 
    class Color(object):
        def __init__(self, red=0: int, green=0: int, blue=0: int, alpha=0: int):
            self._red = None
            self._green = None
            self._blue = None
            self._alpha = None

            self.red = red
            self.green = green
            self.blue = blue
            self.alpha = alpha

        @property
        def red(self):
            return self._red
        
        @red.setter
        def red(self, red: int):
            self._red = move_in_range(red)

        @property
        def green(self):
            return self._green
        
        @green.setter
        def green(self, green: int):
            self._green = move_in_range(green)

        @property
        def blue(self):
            return self._blue
        
        @blue.setter
        def blue(self, blue: int):
            self._blue = move_in_range(blue)

        @property
        def alpha(self):
            return self._alpha
        
        @alpha.setter
        def alpha(self, alpha: int):
            self._alpha = move_in_range(alpha)
        
        def hue(self):
            try:
                if self.red >= self.green >= self.blue:
                    return 60 * (self.green - self.blue) / (self.red - self.blue)
                elif self.green > self.red >= self.blue:
                    return 60 * (2 - (self.red - self.blue) / (self.green - self.blue))
                elif self.green >= self.blue > self.red:
                    return 60 * (2 + (self.blue - self.red) / (self.green - self.red))
                elif self.blue > self.green > self.red:
                    return 60 * (4 - (self.green - self.red) / (self.blue - self.red))
                elif self.blue > self.red >= self.green:
                    return 60 * (4 + (self.red - self.green) / (self.blue - self.green))
                elif self.red >= self.blue > self.green:
                    return 60 * (6 - (self.blue - self.green) / (self.red - self.green))
            
            except ZeroDivisionError:
                return 0

        def saturationHSV(self):
            min = self.min()
            max = self.max()

            try:
                return (max - min) / max * 255
            except ZeroDivisionError:
                return 0
        
        def min(self):
            return min(self.red, self.green, self.blue)

        def max(self):
            return max(self.red, self.green, self.blue)
    
    def move_in_range(n):
        return max(0, min(255, n))
    
    return Color

Color = def_color()