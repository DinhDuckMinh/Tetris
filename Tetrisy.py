import random
#love Figure
class Figure: 
    figures = [
        [[1, 5, 9 ,13], [4, 5, 6, 7]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9],[2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]
# hàm figure
    def __init__(self, x, y):
        self.x= x
        self.y= y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(color) -1)
        self.rotation = 0
#love Tetris
class Tetris:
    level = 2
    score = 0
    state = 'start'
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    figure = None
#hàm khởi tạo
    def __init__(self, height, width):
        self.height = height
        self.width = width
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)
    def new_figure(self):
        self.figure = Figure(3, 0)
    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i + self.figure.y > self.height - 1 or \
                        j + self.figure.x > self.width - 1 or \
                        j + self.figure.x < 0 or \
                            self.field[i + self.figure.y] [j + self.figure.x] > 0:
                    intersection = True
        return intersection
#
    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] =  self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            game.state = 'gameover'

