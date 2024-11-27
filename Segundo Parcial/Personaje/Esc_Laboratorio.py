from manim import *

class Piso(VGroup):
    def __init__(self, frame_width, frame_height, tile_size=0.5, num_tiles_x=10, num_tiles_y=6, **kwargs):
        super().__init__(**kwargs)
        self.tile_size = tile_size
        self.num_tiles_x = int(frame_width / tile_size) + num_tiles_x
        self.num_tiles_y = num_tiles_y
        self.crear_azulejos(frame_width, frame_height)
    
    def crear_azulejos(self, frame_width, frame_height):
        for i in range(self.num_tiles_x):
            for j in range(self.num_tiles_y):
                color = GRAY_A if (i + j) % 2 == 0 else WHITE
                tile = Square(side_length=self.tile_size).set_fill(color, opacity=1)
                tile.set_stroke(GRAY, width=0.5)
                tile.move_to(np.array([
                    i * self.tile_size - frame_width / 2 + self.tile_size / 2,
                    j * self.tile_size - frame_height / 2 + self.tile_size / 2 - 1,
                    0
                ]))
                self.add(tile)
        
        perspective_matrix = [[1, 0.5, 0], [0, 1, 0], [0, 0, 1]]
        self.apply_matrix(perspective_matrix)

class Pared(Rectangle):
    def __init__(self, frame_width, **kwargs):
        super().__init__(width=frame_width, height=5.5, **kwargs)
        self.set_fill(GRAY, opacity=0.8)
        self.to_edge(UP)

class Escritorio(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pata_izquierda = Rectangle(width=0.3, height=1).set_fill(DARK_BROWN, opacity=1).move_to(DOWN * 2 + RIGHT * 4.2)
        pata_derecha = Rectangle(width=0.3, height=1).set_fill(DARK_BROWN, opacity=1).move_to(DOWN * 2 + RIGHT * 5.8)
        superficie = Rectangle(width=3, height=0.4).set_fill(DARK_BROWN, opacity=1).move_to(DOWN * 1.5 + RIGHT * 5)
        
        self.add(pata_izquierda, pata_derecha, superficie)
        
        monitor = Rectangle(width=1.2, height=0.8).set_fill(BLUE_E, opacity=0.9).move_to(superficie.get_top() + UP * 0.6)
        base_monitor = Rectangle(width=0.2, height=0.3).set_fill(GRAY, opacity=1).next_to(monitor, DOWN, buff=0.05)
        
        self.add(monitor, base_monitor)

class Ventana(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ventana = Rectangle(width=3, height=1.5).set_fill(WHITE, opacity=0.5).to_edge(UP).shift(DOWN * 0.5)
        lineas_verticales = VGroup(
            Line(ventana.get_top(), ventana.get_bottom()).shift(LEFT * 1),
            Line(ventana.get_top(), ventana.get_bottom()).shift(RIGHT * 1)
        )
        lineas_horizontales = VGroup(
            Line(ventana.get_left(), ventana.get_right()).shift(UP * 0.5),
            Line(ventana.get_left(), ventana.get_right()).shift(DOWN * 0.5)
        )
        self.add(ventana, lineas_verticales, lineas_horizontales)

class Librero(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        estante_principal = Rectangle(width=1.2, height=3.5).set_fill(DARK_BROWN, opacity=1).to_edge(LEFT).shift(DOWN * 0.5)
        self.add(estante_principal)
        
        for i in range(5):
            estante = Line(start=LEFT, end=RIGHT, color=WHITE, stroke_width=4).set_length(1.1)
            estante.move_to(estante_principal.get_top() + DOWN * (0.3 + 0.6 * i))
            self.add(estante)
        
        colores = [RED, BLUE, GREEN, YELLOW]
        for i in range(4):
            for j in range(3):
                libro = Rectangle(width=0.15, height=0.5).set_fill(colores[j % len(colores)], opacity=1)
                libro.move_to(estante_principal.get_top() + DOWN * (0.6 * (i + 1)) + RIGHT * (0.35 * (j - 1)))
                self.add(libro)

class EscenaLaboratorio(Scene):
    def construct(self):
        frame_width = self.camera.frame_width
        frame_height = self.camera.frame_height
        piso = Piso(frame_width, frame_height)
        pared = Pared(frame_width)
        escritorio = Escritorio()
        ventana = Ventana()
        librero = Librero()
        
        self.add(piso, pared, escritorio, ventana, librero)
