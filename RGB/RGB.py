class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}•{self.END}{self.MOD}'

    def __eq__(self, other):
        if self.red == other.red and self.green == other.green and self.blue == other.blue:
            return True
        else:
            return False

    def __add__(self, other):
        return type(self)(min(self.red + other.red, 255),
                          min(self.green + other.green, 255),
                          min(self.blue + other.blue, 255))

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __mul__(self, c):
        cl = -256 * (1 - c)
        F = 259 * (cl + 255) / (255 * (259 - cl))
        return type(self)(int(F * (self.red - 128) + 128),
                          int(F * (self.green - 128) + 128),
                          int(F * (self.blue - 128) + 128))

    def __rmul__(self, c):
        return self * c


if __name__ == '__main__':
    # вывод цвета
    red = Color(255, 0, 0)
    print(red)

    # сравнение цветов
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red == green)
    print(red == Color(255, 0, 0))

    # смешивание цветов
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red + green)

    # уникальные цвета
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(set(color_list))

    # уменьшение контраста
    red = Color(255, 0, 0)
    print(red, 0.5 * red)




