from manim import *


class Stack(Scene):
    """
    This module defines the Stack class for manim, which allows easy stack visualization.
    """
    def construct(self):
        """
        Unused driver code.
        :return: None
        """
        stack = Group()

        for i in range(5):
            rect = Rectangle(width=1, height=0.33)
            rect.set_stroke(ORANGE)
            text = Text("Test", color=ORANGE).scale(0.33)
            text.move_to(rect.get_center())
            ele = Group(rect, text)
            self.push(stack, ele)

        for i in range(5):
            self.pop(stack)

    def push(self, stack, text):
        """
        This allows you to push an element to the stack. Each element is a
        rectangle of width 1 and height 1/3.
        TODO: Set width and height in Stack constructor.
        :param stack: The stack who you will be pushing to
        :param text: The text to go inside the stack element.
        :return: None
        """
        rect = Rectangle(width=1, height=0.33)
        rect.set_stroke(BLUE)
        text = Text(text, color=WHITE).scale(0.30)
        text.move_to(rect.get_center())
        ele = Group(rect, text)

        if len(stack) == 0:
            ele.move_to(ORIGIN + RIGHT * 6.0 + DOWN)
        else:
            ele.move_to(stack.get_top() + (UP * 0.33 / 2))

        stack.add(ele)
        self.play(Create(rect), Write(text))

    def quick_push(self, stack, text):
        """
        This allows you to quickly push an element to the stack. Each element is a
        rectangle of width 1 and height 1/3. The difference between quick and
        regular push is that quick push doesn't do any 'self.play' stuff.
        This method is for use in conjuction with text replacement.
        TODO: Set width and height in Stack constructor.
        :param stack: The stack who you will be pushing to
        :param text: The text to go inside the stack element.
        :return: None
        """
        rect = Rectangle(width=1, height=0.33)
        rect.set_stroke(BLUE)
        text = Text(text, color=WHITE).scale(0.30)
        text.move_to(rect.get_center())
        ele = Group(rect, text)

        if len(stack) == 0:
            ele.move_to(ORIGIN + RIGHT * 6.0 + DOWN)
        else:
            ele.move_to(stack.get_top() + (UP * 0.33 / 2))

        stack.add(ele)
        self.add(rect, text)

    def change(self, stack, new_text):
        """
        This method lets you change the text inside the top stack element.
        :param stack: The stack to change the top element in.
        :param new_text: The text to replace the old text and be displayed.
        :return: None
        """
        # needs to be rewritten
        if len(stack) > 0:
            element = stack[-1]
            rect = element[0]
            new_element_text = Text(new_text).scale(0.30)
            new_element_text.move_to(rect.get_center())

            self.remove(element[0])
            self.remove(element[1])
            self.add(rect)
            self.play(Write(new_element_text))

            new_element = Group(rect, new_element_text)
            stack.add(new_element)

    def pop(self, stack):
        """
        This allows you to pop an element from the stack.
        TODO: Set width and height in Stack constructor.
        :param stack: The stack who you will be pushing to.
        :return: None
        """
        if len(stack) > 0:
            element = stack[-1]
            self.play(FadeOut(element))
            stack.remove(element)

    def quick_pop(self, stack):
        """
        This allows you to quickly pop an element from the stack. This is to be
        used in conjuction with the change method to make sure everything works
        as intended.
        TODO: Set width and height in Stack constructor.
        :param stack: The stack who you will be pushing to.
        :return: None
        """
        if len(stack) > 0:
            element = stack[-1]
            self.remove(element)
            stack.remove(element)
