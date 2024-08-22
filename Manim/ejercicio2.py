from manim import *

class SecondScene(Scene):
    def construct(self):
        text = MathTex("x^2")
        self.add(text)