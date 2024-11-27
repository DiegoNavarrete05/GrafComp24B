from manim import *

class Cielo(Rectangle):
    def __init__(self, frame_width, frame_height, **kwargs):
        super().__init__(width=frame_width, height=frame_height, **kwargs)
        self.set_fill(BLUE, opacity=1)
        self.to_edge(UP)

class Pradera(Rectangle):
    def __init__(self, frame_width, **kwargs):
        super().__init__(width=frame_width, height=3, **kwargs)
        self.set_fill(GREEN, opacity=1)
        self.to_edge(DOWN)

class Sol(Circle):
    def __init__(self, **kwargs):
        super().__init__(radius=0.6, **kwargs)
        self.set_fill(YELLOW, opacity=1)
        self.set_stroke(color=ORANGE, width=4)
        self.move_to(UP * 3.5 + RIGHT * 5)

class Arbol(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        tronco = Rectangle(width=0.3, height=1.5).set_fill(DARK_BROWN, opacity=1)
        tronco.move_to(DOWN * 1.5 + LEFT * 2)
        follaje = Circle(radius=1).set_fill(GREEN, opacity=1)
        follaje.move_to(tronco.get_top() + UP * 0.5)
        self.add(tronco, follaje)

class CaminoDePiedras(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        piedra_color = GRAY
        for i in range(6):
            piedra = Ellipse(width=0.5, height=0.2).set_fill(piedra_color, opacity=1)
            piedra.move_to(DOWN * (1 + 0.5 * i) + LEFT * (0.5 * i))
            self.add(piedra)

class Nube(Ellipse):
    def __init__(self, width=2, height=0.7, **kwargs):
        super().__init__(width=width, height=height, **kwargs)
        self.set_fill(WHITE, opacity=0.8)

class MiGelipeEnBosque(Scene):
    def construct(self):
        frame_width = self.camera.frame_width
        frame_height = self.camera.frame_height
        
        cielo = Cielo(frame_width, frame_height)
        pradera = Pradera(frame_width)
        sol = Sol()
        arbol = Arbol()
        camino = CaminoDePiedras()
        
        nubes = VGroup(
            Nube().move_to(UP * 3 + LEFT * 5),
            Nube().move_to(UP * 2.5 + LEFT * 3),
            Nube().move_to(UP * 2 + LEFT * 1)
        )
        
        self.add(cielo, pradera, sol, arbol, camino, nubes)
