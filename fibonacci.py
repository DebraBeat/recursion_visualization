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


class FibonacciWithStack(Scene):
    def construct(self):
        colors = [BLUE, GOLD, GREEN, PINK, TEAL]
        color_index = 0
        stack = Group()
        group = Group()
        cs = []  # call stack

        def push(element):
            if len(stack) == 0:
                element.move_to(ORIGIN + RIGHT * 6.0)
            else:
                element.move_to(stack.get_top() + (UP * 0.33 / 2))

            stack.add(element)
            self.play(FadeIn(element))

        def pop():
            if len(stack) > 0:
                element = stack[-1]
                self.play(FadeOut(element))
                stack.remove(element)

        def top():
            return stack[-1]

        # Begin main part of program
        # In this program, we'll go through the fibonacci of four
        fib_idx = 4

        intro_text = Text(f'Start with Fibonacci of {fib_idx}')
        intro_text.shift(UP)
        self.play(FadeIn(intro_text))
        self.wait(1)
        self.play(FadeOut(intro_text))


        left = Text(f'fib({fib_idx}) =')
        self.play(FadeIn(left))
        self.play(left.animate.shift(UP * 0.5))

        # Initialize stack through first iteration

        stack_text = Text('Stack', color=ORANGE)
        stack_text.move_to(ORIGIN + RIGHT * 6.0)
        stack_text.shift(UP * 3.0)
        self.play(FadeIn(stack_text))
        self.wait(1)


        rect = Rectangle(width=1, height=0.33)
        rect.set_stroke(ORANGE)
        text = Text(f'fib({fib_idx})', color=ORANGE).scale(0.33)
        text.move_to(rect.get_center())
        ele = Group(rect, text)
        push(ele)
        cs.append(fib_idx)
        self.wait(1)

        right = Text(f'fib({fib_idx - 1}) + fib({fib_idx - 2})').shift(DOWN * 0.5)

        self.play(FadeIn(right))
        self.wait(1)

        rect = Rectangle(width=1, height=0.33)
        rect.set_stroke(ORANGE)
        text = Text(f'fib({fib_idx - 1})', color=ORANGE).scale(0.33)
        text.move_to(rect.get_center())
        ele = Group(rect, text)
        push(ele)
        cs.append(fib_idx - 1)
        self.wait(1)

        rect = Rectangle(width=1, height=0.33)
        rect.set_stroke(ORANGE)
        text = Text(f'fib({fib_idx - 2})', color=ORANGE).scale(0.33)
        text.move_to(rect.get_center())
        ele = Group(rect, text)
        push(ele)
        cs.append(fib_idx - 2)
        self.wait(1)

        while cs:
            curr = cs.pop()
