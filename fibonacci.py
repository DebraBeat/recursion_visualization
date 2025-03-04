from manim import *
import numpy as np

hashmap = {0: 1, 1: 1}


def fib(i: int) -> int:
    if i in hashmap:
        return hashmap[i]

    hashmap[i] = fib(i - 1) + fib(i - 2)

    return hashmap[i]

# TODO:
#       - Add Stack vis
#       - Add Binary Tree vis


class Stack(Scene):

    def pop(self):
        pass

    def push(self):
        pass

    def top(self):
        pass


class Fibonacci(Scene):
    def construct(self):
        colors = [BLUE, GOLD, GREEN, PINK, TEAL]
        color_index = 0
        scale_factor = 1
        group = Group()

        for i in range(0, 10):
            curr_fib = np.sqrt(fib(i))
            # next_fib = np.sqrt(fib(i + 1))
            scale_factor = 1.0 / curr_fib
            # next_scale_factor = 1.0 / next_fib
            # next_rect = Rectangle(width=next_fib, height=next_fib).scale(next_scale_factor)

            rect = Rectangle(width=curr_fib, height=curr_fib).scale(scale_factor)
            rect.set_fill(colors[color_index], opacity=0.5)
            color_index = (color_index + 1) % len(colors)

            t = Text(f'{i}')
            b = Brace(rect)
            b_text = Text(f'{fib(i)}')
            f_text = Text(f'Fibonacci of {i}')
            f_text.shift(DOWN * 1.5)
            b_text.shift(DOWN * 1.25)
            t.shift(UP)

            self.play(FadeIn(t))
            self.play(group.animate.scale(scale_factor))
            self.play(Create(rect))
            self.play(FadeIn(b, f_text))
            self.play(FadeOut(f_text))
            self.play(FadeIn(b_text))
            self.wait(1)

            rect = Group(rect, t, b, b_text)
            group.add(rect)
            self.play(group.animate.shift(LEFT))
