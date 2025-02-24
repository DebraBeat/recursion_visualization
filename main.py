from manim import *

# TODO incorporate hashmap into manim visualization
hashmap = {0: 1, 1: 1}

def fib(i : int) -> int:
    if i == 0 or i == 1:
        return 1

    return fib(i - 1) + fib(i - 2)

# TODO: - Add iterator above each square
#       - Create stack visualization
#       - Potentially add code into visualization
class CreateRectangle(Scene):
    def construct(self):
        colors = [BLUE, GOLD, GREEN, PINK, TEAL]
        color_index = 0
        # TODO
        #       - Animate rectangle movement

        # NOTE: This is to initialize the variable "prev_rect"
        # it is not displayed.
        scale_factor = 1
        group = Group()

        for i in range(0, 10):
            curr_fib = fib(i)
            next_fib = fib(i + 1)
            scale_factor = 1.0 / curr_fib
            next_scale_factor = 1.0 / next_fib
            next_rect = Rectangle(width=next_fib, height=next_fib).scale(next_scale_factor)

            rect = Rectangle(width=curr_fib, height=curr_fib).scale(scale_factor)
            rect.set_fill(colors[color_index], opacity=0.5)
            color_index = (color_index + 1) % len(colors)

            self.play(group.animate.scale(scale_factor))
            self.play(Create(rect))
            self.wait(1.5)
            group.add(rect)
            self.play(group.animate.next_to(next_rect, LEFT, buff=0))