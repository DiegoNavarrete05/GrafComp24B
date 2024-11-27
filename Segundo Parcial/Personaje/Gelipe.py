from manim import *

class main(Scene):
    def construct(self):
        # Tamaño de cada azulejo
        nombre = Text("Gelipe",font_size=26)
        nombre.move_to(ORIGIN + UP)
        self.add(nombre)
        tile_size = 0.5
        num_tiles_x = int(config.frame_width / tile_size) + 10  # Aumentar número de azulejos en X para cubrir el ancho
        num_tiles_y = 6  # Número de filas de azulejos

        # Crear el piso de azulejos intercalados
        tiles = VGroup()
        for i in range(num_tiles_x):
            for j in range(num_tiles_y):
                color = GRAY_A if (i + j) % 2 == 0 else WHITE
                tile = Square(side_length=tile_size).set_fill(color, opacity=1)
                tile.set_stroke(GRAY, width=0.5)  # Borde del azulejo
                tile.move_to(np.array([
                    i * tile_size - config.frame_width / 2 + tile_size / 2,
                    j * tile_size - config.frame_height / 2 + tile_size / 2 - 1,  # Mover el piso más abajo
                    0
                ]))
                tiles.add(tile)

        # Aplicar perspectiva inclinada
        perspective_matrix = [[1, 0.5, 0], [0, 1, 0], [0, 0, 1]]
        tiles.apply_matrix(perspective_matrix)
        self.add(tiles)

        # Fondo del laboratorio (pared)
        pared = Rectangle(width=config.frame_width, height=5.5).set_fill(GRAY, opacity=0.8)
        pared.to_edge(UP)  # Coloca la pared en la parte superior
        self.add(pared)

        # Pata izquierda
        pata_izquierda = Rectangle(width=0.3, height=1).set_fill(DARK_BROWN, opacity=1)
        pata_izquierda.move_to(DOWN * 2 + RIGHT * 4.2)  # Ajusta la posición de la pata izquierda
        self.add(pata_izquierda)

        # Pata derecha
        pata_derecha = Rectangle(width=0.3, height=1).set_fill(DARK_BROWN, opacity=1)
        pata_derecha.move_to(DOWN * 2 + RIGHT * 5.8)  # Ajusta la posición de la pata derecha
        self.add(pata_derecha)

        # Escritorio
        escritorio = Rectangle(width=3, height=0.4).set_fill(DARK_BROWN, opacity=1)
        escritorio.move_to(DOWN * 1.5 + RIGHT * 5)  # Coloca el escritorio en la parte inferior central
        self.add(escritorio)

        # Monitor (computadora)
        monitor = Rectangle(width=1.2, height=0.8).set_fill(BLUE_E, opacity=0.9)
        monitor.move_to(escritorio.get_top() + UP * 0.6)  # Encima del escritorio
        self.add(monitor)

        # Base del monitor (la torre o soporte)
        base_monitor = Rectangle(width=0.2, height=0.3).set_fill(GRAY, opacity=1)
        base_monitor.next_to(monitor, DOWN, buff=0.05)
        self.add(base_monitor)

        # Ventana en la pared
        ventana = Rectangle(width=3, height=1.5).set_fill(WHITE, opacity=0.5)
        ventana.to_edge(UP).shift(DOWN * 0.5)  # Ventana en la parte superior de la pared
        self.add(ventana)

        # Detalles en la ventana (rejilla)
        lineas_verticales = VGroup(
            Line(ventana.get_top(), ventana.get_bottom()).shift(LEFT * 1),
            Line(ventana.get_top(), ventana.get_bottom()).shift(RIGHT * 1)
        )
        lineas_horizontales = VGroup(
            Line(ventana.get_left(), ventana.get_right()).shift(UP * 0.5),
            Line(ventana.get_left(), ventana.get_right()).shift(DOWN * 0.5)
        )
        self.add(lineas_verticales, lineas_horizontales)

        # Librero (estructura del librero)
        estante_principal = Rectangle(width=1.2, height=3.5).set_fill(DARK_BROWN, opacity=1)
        estante_principal.to_edge(LEFT).shift(DOWN * 0.5)  # Colocar en el lado izquierdo
        self.add(estante_principal)

        # Crear los estantes usando un bucle for
        for i in range(5):  # 5 estantes
            estante = Line(start=LEFT, end=RIGHT, color=WHITE, stroke_width=4).set_length(1.1)
            estante.move_to(estante_principal.get_top() + DOWN * (0.3 + 0.6 * i))  # Ajuste de la posición para cada estante
            self.add(estante)

        # Libros (rectángulos de colores que representan libros en los estantes)
        libros = []
        colores = [RED, BLUE, GREEN, YELLOW]
        for i in range(4):  # Cuatro estantes
            for j in range(3):  # Tres libros por estante
                libro = Rectangle(width=0.15, height=0.5).set_fill(colores[j % len(colores)], opacity=1)
                libro.move_to(estante_principal.get_top() + DOWN * (0.6 * (i + 1)) + RIGHT * (0.35 * (j - 1)))
                libros.append(libro)

        # Añadir los libros a la escena
        self.add(*libros)


        # Crear el cuerpo principal como una elipse
        cuerpo = Ellipse(width=5, height=2, color=BLUE, fill_opacity=1)
        cuerpo.shift(DOWN * 0.5)  # Bajar el cuerpo
        self.play(Create(cuerpo))
        self.wait(1)

        # Crear los ojos
        ojo1 = Polygon([-0.7, -0.1, 0], [-0.2, -0.1, 0], [-0.45, -0.5, 0], color=WHITE, fill_opacity=1)
        ojo2 = Polygon([0.7, -0.1, 0], [0.2, -0.1, 0], [0.45, -0.5, 0], color=WHITE, fill_opacity=1)
        ojo1.shift(LEFT * 0.35 + DOWN * 0.01)  # Ajustar el ojo izquierdo
        ojo2.shift(RIGHT * 0.35 + DOWN * 0.01)  # Ajustar el ojo derecho
        self.play(Create(ojo1), Create(ojo2))
        self.wait(1)

        # Crear los brazos
        brazo1 = RoundedRectangle(width=2, height=0.5, color=BLUE, fill_opacity=1)
        brazo2 = RoundedRectangle(width=2, height=0.5, color=BLUE, fill_opacity=1)

        brazo1.rotate(PI / 8)
        brazo2.rotate(-PI / 8)

        brazo1.shift(LEFT * 3 + DOWN * 1)  # Bajar los brazos
        brazo2.shift(RIGHT * 3 + DOWN * 1)
        self.play(Create(brazo1), Create(brazo2))
        self.wait(1)

        # Crear las piernas
        pierna1 = Square(side_length=0.7, color=BLUE, fill_opacity=1)
        pierna2 = Square(side_length=0.7, color=BLUE, fill_opacity=1)

        pierna1.shift(LEFT * 0.75 + DOWN * 1.7)
        pierna2.shift(RIGHT * 0.75 + DOWN * 1.7)
        self.play(Create(pierna1), Create(pierna2))
        self.wait(1)

        # Crear los pies
        pie1 = Polygon([0, 0, 0], [0.5, -0.5, 0], [-0.5, -0.5, 0], color=BLUE, fill_opacity=1)
        pie2 = Polygon([0, 0, 0], [0.5, -0.5, 0], [-0.5, -0.5, 0], color=BLUE, fill_opacity=1)

        pie1.shift(LEFT * 0.75 + DOWN * 2.1)
        pie2.shift(RIGHT * 0.75 + DOWN * 2.1)
        self.play(Create(pie1), Create(pie2))
        self.wait(1)

        # Crear la boca como una flecha curva doble
        flecha_curva_doble = CurvedDoubleArrow(
            start_point=LEFT * 0.8, end_point=RIGHT * 0.8, color=YELLOW, angle=-PI / 2
        )
        flecha_curva_doble.shift(DOWN * 1.2)  # Colocar la flecha curva doble más abajo
        flecha_curva_doble.scale(0.7)  # Ajustar el tamaño de la "boca"
        self.play(Create(flecha_curva_doble))
        self.wait(1)

        # Agrupar pierna1 y pie1 para moverlos juntos
        pierna_y_pie1 = VGroup(pierna1, pie1)

        # Animación para levantar el brazo derecho y mover la pierna y el pie juntos
        punto_fijo_brazo2 = brazo2.get_left()  # Mantener este punto fijo
        punto_fijo_pierna1 = pierna1.get_top()  # Punto fijo para rotar la pierna desde la parte superior
        punto_fijo_boca1 = flecha_curva_doble.get_top()

        # Agrupar las animaciones
        animaciones = AnimationGroup(
            Rotate(brazo2, angle=PI / 3, about_point=punto_fijo_brazo2),
            Rotate(pierna_y_pie1, angle=-PI / 6, about_point=punto_fijo_pierna1),
            Rotate(flecha_curva_doble, angle= 2*PI / 2, about_point=punto_fijo_boca1)  # Girar hacia arriba para sonreír
        )

        self.play(animaciones)
        self.wait(0.5)

        # Regresar a la posición original
        animaciones_invertidas = AnimationGroup(
            Rotate(brazo2, angle=-PI / 3, about_point=punto_fijo_brazo2),
            Rotate(pierna_y_pie1, angle=PI / 6, about_point=punto_fijo_pierna1),
            Rotate(flecha_curva_doble, angle= -2*PI / 2, about_point=punto_fijo_boca1)  # Regresar a la posición original
        )

        self.play(animaciones_invertidas)


        # Esperar antes de finalizar la escena
        self.wait(5)
