import math
from contextlib import redirect_stdout

from manim import *


def find(element, input_list):
    result = [i for i, x in enumerate(input_list) if x == element]
    return result[0] if result else -1


def coord_by_id(i, n):
    angle = 2 * PI * i / n
    amplitude = 2
    return amplitude * math.cos(angle), amplitude * math.sin(angle)


class GraphWithWayCreator(Scene):
    def __init__(self, way):
        self.way = way
        super().__init__()

    def construct(self):
        self.camera.background_color = WHITE
        radius = .3
        n = len(self.way)
        for i in range(n):
            coord = coord_by_id(i, n)

            circle = Circle(radius=radius, color=BLUE)
            circle.set_fill(opacity=.15)
            number_text = Text(f'{i}', font_size=32, color=BLACK)

            circle.set_x(coord[0])
            circle.set_y(coord[1])
            number_text.set_x(coord[0])
            number_text.set_y(coord[1])

            self.play(GrowFromCenter(circle), GrowFromCenter(number_text), run_time=.1)
        self.wait(.1)

        for i in range(n):
            for j in range(i + 1, n):
                dot1, dot2 = Dot(), Dot()
                coord1, coord2 = list(coord_by_id(i, n)), list(coord_by_id(j, n))
                dist = math.hypot(coord2[0] - coord1[0], coord2[1] - coord1[1])
                e = [(coord2[0] - coord1[0]) / dist, (coord2[1] - coord1[1]) / dist]
                for k in range(2):
                    coord1[k] += e[k] * radius
                    coord2[k] -= e[k] * radius
                    [dot1.set_x, dot1.set_y][k](coord1[k])
                    [dot2.set_x, dot2.set_y][k](coord2[k])
                line_color = BLUE_D if self.way[((k := find(i, self.way)) + 1) % n] == j or self.way[k - 1] == j \
                    else LIGHT_GRAY
                line = Line(dot1, dot2, color=line_color)

                self.add(line)
                self.wait(.1)
        self.wait(1)


def draw_with_cyclic_way(way):
    log_file_name = 'log.txt'
    with open(log_file_name, 'w') as f:
        print(f'Логи построения графа сохраняются в файле: {log_file_name}')
        with redirect_stdout(f):
            with tempconfig({"quality": "medium_quality", "preview": True}):
                scene = GraphWithWayCreator(way)
                scene.render()
