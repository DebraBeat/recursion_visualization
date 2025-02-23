from manim import *
import numpy as np

# TODO incorporate hashmap into manim visualization
hashmap = {0: 1, 1: 1}

def fib(i : int) -> int:
    if i == 0 or i == 1:
        return 1

    return fib(i - 1) + fib(i - 2)
class CreateRectangle(Scene):
    def construct(self):
        colors = [BLUE, GOLD, GREEN, PINK, TEAL]
        color_index = 0
        # TODO  - Incorporate this as a list instead of rewriting the rectangle
        #       Or use transform (possibly) to just have a "current"
        #       and "previous" rectangle
        #       - Animate rectangle movement
        for i in range(0, 10):
            rect = Rectangle(width=np.sqrt(fib(i)), height=np.sqrt(fib(i)))
            rect.set_fill(colors[color_index], opacity=0.5)
            color_index = (color_index + 1) % len(colors)

            self.play(Create(rect))
            self.wait(2)
            rect.move_to(RIGHT)
