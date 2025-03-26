from manim import *
import numpy as np

hashmap = {0: 1, 1: 1}


def fib(i: int) -> int:
    if i in hashmap:
        return hashmap[i]

    hashmap[i] = fib(i - 1) + fib(i - 2)

    return hashmap[i]


class FibonacciRegular(Scene):
    def construct(self):
        colors = [BLUE, GOLD, GREEN, PINK, TEAL]
        color_index = 0
        scale_factor = 1
        group = Group()

        intro_text = Text("The Fibonacci sequence is a sequence of numbers named after "
                          "the mathematician\n \"Fibonacci\" (he only had one word for "
                          "his name).", font_size=20)
        intro_text.shift(UP * 2.0)

        definition_text = Text("The sequence is defined as follows:                         "
                               "\n\n Let the "
                               "first two elements each be equal to one.\n Every "
                               "element afterwards is the sum of the previous "
                               "two.\n In other words F_0 = 1, F_1 = 1, F_n = "
                               "F_{n-1} + F_{n-2}", font_size=20)

        transition_text = Text("If we set make squares with the length of a side being"
                               "a fibonacci number we get the following:", font_size=20)

        self.play(Write(intro_text))
        self.wait(5)
        self.play(Write(definition_text))
        self.wait(5)
        self.play(FadeOut(intro_text))
        self.play(FadeOut(definition_text))

        self.play(Write(transition_text))
        self.wait(2)
        self.play(FadeOut(transition_text))

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
            equals = Text('=')
            b_text = Text(f'{fib(i)}')
            f_text = Text(f'Fibonacci of {i}')
            f_text.shift(DOWN * 1.6)
            equals.shift(DOWN * 1.25)
            b_text.shift(DOWN * 1.25)
            t.shift(UP)

            self.play(FadeIn(t))
            self.play(group.animate.scale(scale_factor))
            self.play(Create(rect))
            self.play(FadeIn(b, f_text))
            self.play(FadeOut(f_text))
            self.play(FadeIn(equals))
            self.play(FadeOut(equals))
            self.play(FadeIn(b_text))
            self.wait(1)

            rect = Group(rect, t, b, b_text)
            group.add(rect)
            self.play(group.animate.shift(LEFT))


class FibonacciWithStack(Scene):
    def push(self, stack, element):
        if len(stack) == 0:
            element.move_to(ORIGIN + RIGHT * 6.0)
        else:
            element.move_to(stack.get_top() + (UP * 0.33 / 2))

        stack.add(element)
        self.play(FadeIn(element))

    def pop(self, stack):
        if len(stack) > 0:
            element = stack[-1]
            self.play(FadeOut(element))
            stack.remove(element)

    def top(self, stack):
        return stack[-1]

    def get_vertex(self, num):
        return Group()
    def construct(self):
        colors = [BLUE, GOLD, GREEN, PINK, TEAL]
        color_index = 0
        stack = Group()
        group = Group()
        cs = []  # call stack

        # Begin main part of program
        # In this program, we'll go through the fibonacci of four
        fib_idx = 4

        intro_text = Text(f'Fibonacci of {fib_idx} using stacks and trees')
        intro_text.shift(UP)
        self.play(Write(intro_text))
        self.wait(1)
        self.play(FadeOut(intro_text))

        stack_text = Text('Stack', color=ORANGE)
        stack_text.move_to(ORIGIN + RIGHT * 6.0)
        stack_text.shift(UP * 3.0)
        self.play(FadeIn(stack_text))
        self.wait(1)
