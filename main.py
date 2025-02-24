from manim import *
import numpy as np

# TODO incorporate hashmap into manim visualization
hashmap = {0: 1, 1: 1}

def fib(i : int) -> int:
    if i == 0 or i == 1:
        return 1

    return fib(i - 1) + fib(i - 2)

# TODO: - Add iterator above each square
#       - Create stack visualization
#       - Potentially add code into visualization
class Fibonacci(Scene):
    def construct(self):
        colors = [BLUE, GOLD, GREEN, PINK, TEAL]
        color_index = 0
        scale_factor = 1
        group = Group()

        for i in range(0, 10):
            curr_fib = np.sqrt(fib(i))
            next_fib = np.sqrt(fib(i + 1))
            scale_factor = 1.0 / curr_fib
            next_scale_factor = 1.0 / next_fib
            next_rect = Rectangle(width=next_fib, height=next_fib).scale(next_scale_factor)

            rect = Rectangle(width=curr_fib, height=curr_fib).scale(scale_factor)
            rect.set_fill(colors[color_index], opacity=0.5)
            color_index = (color_index + 1) % len(colors)

            t = Text(f'{i}')
            b = Brace(rect)
            b_text = Text(f'{fib(i)}')
            b_text.shift(DOWN * 1.5)
            t.shift(UP)

            self.play(FadeIn(t))
            self.play(group.animate.scale(scale_factor))
            self.play(Create(rect))
            self.play(FadeIn(b, b_text))
            self.wait(1.5)

            rect = Group(rect, t, b, b_text)
            group.add(rect)
            self.play(group.animate.shift(LEFT))