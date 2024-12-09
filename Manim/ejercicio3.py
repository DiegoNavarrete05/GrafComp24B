from manim import *

class ThreeScene(Scene):
    def construct(self):
        text = MathTex(r"X = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
        self.add(text)
#Revisado
