from manim import *
import numpy as np

class Shapes(Scene):
  def construct(self):
    circulo = Circle() # Creación de circulo
    createCircle = Create(circulo) # Animación de creación
    self.play(createCircle) # Mostrar la animación
    fadeOutCircle = FadeOut(circulo) # Animación de desaparición
    self.play(fadeOutCircle) # Mostrar la animación

    rect = Rectangle(color="red", height=3, width=1)
    self.play(Create(rect))
    self.play(FadeOut(rect))