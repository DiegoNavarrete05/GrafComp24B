from manim import *

class main(Scene):
    def construct(self):
        # Definir el color del robot Gelipe
        COLOR_GELIPE = BLUE
        
        # Tamaño de cada azulejo
        tile_size = 0.5
        # Calcular el número de azulejos necesarios para cubrir el ancho y definir el número de filas
        num_tiles_x = int(config.frame_width / tile_size) + 10  # Aumentar el número de azulejos en X
        num_tiles_y = 6  # Definir el número de filas de azulejos

        # Crear el piso con azulejos intercalados
        tiles = VGroup()
        for i in range(num_tiles_x):
            for j in range(num_tiles_y):
                # Alternar el color de los azulejos entre GRAY_A y WHITE
                color = GRAY_A if (i + j) % 2 == 0 else WHITE
                tile = Square(side_length=tile_size).set_fill(color, opacity=1)  # Crear un azulejo
                tile.set_stroke(GRAY, width=0.5)  # Añadir un borde al azulejo
                tile.move_to(np.array([  # Posicionar el azulejo
                    i * tile_size - config.frame_width / 2 + tile_size / 2,
                    j * tile_size - config.frame_height / 2 + tile_size / 2 - 1,  # Ajustar la altura del piso
                    0
                ]))
                tiles.add(tile)  # Añadir el azulejo al grupo de azulejos

        # Aplicar perspectiva inclinada al piso
        perspective_matrix = [[1, 0.5, 0], [0, 1, 0], [0, 0, 1]]
        tiles.apply_matrix(perspective_matrix)
        self.add(tiles)  # Añadir el piso a la escena

        # Crear la pared de fondo del laboratorio
        pared = Rectangle(width=config.frame_width, height=5.5).set_fill(GRAY, opacity=0.8)
        pared.to_edge(UP)  # Posicionar la pared en la parte superior
        self.add(pared)

        # Crear las patas del escritorio
        pata_izquierda = Rectangle(width=0.3, height=1).set_fill(DARK_BROWN, opacity=1)
        pata_izquierda.move_to(DOWN * 2 + RIGHT * 4.2)  # Ajustar la posición de la pata izquierda
        self.add(pata_izquierda)

        pata_derecha = Rectangle(width=0.3, height=1).set_fill(DARK_BROWN, opacity=1)
        pata_derecha.move_to(DOWN * 2 + RIGHT * 5.8)  # Ajustar la posición de la pata derecha
        self.add(pata_derecha)

        # Crear el escritorio
        escritorio = Rectangle(width=3, height=0.4).set_fill(DARK_BROWN, opacity=1)
        escritorio.move_to(DOWN * 1.5 + RIGHT * 5)  # Posicionar el escritorio
        self.add(escritorio)

        # Crear el monitor sobre el escritorio
        monitor = Rectangle(width=1.2, height=0.8).set_fill(BLUE_E, opacity=0.9)
        monitor.move_to(escritorio.get_top() + UP * 0.6)  # Colocar el monitor encima del escritorio
        self.add(monitor)

        # Base del monitor
        base_monitor = Rectangle(width=0.2, height=0.3).set_fill(GRAY, opacity=1)
        base_monitor.next_to(monitor, DOWN, buff=0.05)  # Posicionar la base debajo del monitor
        self.add(base_monitor)

        # Crear una ventana en la pared
        ventana = Rectangle(width=3, height=1.5).set_fill(WHITE, opacity=0.5)
        ventana.to_edge(UP).shift(DOWN * 0.5)  # Posicionar la ventana en la parte superior de la pared
        self.add(ventana)

        # Crear detalles (rejilla) en la ventana
        lineas_verticales = VGroup(
            Line(ventana.get_top(), ventana.get_bottom()).shift(LEFT * 1),
            Line(ventana.get_top(), ventana.get_bottom()).shift(RIGHT * 1)
        )
        lineas_horizontales = VGroup(
            Line(ventana.get_left(), ventana.get_right()).shift(UP * 0.5),
            Line(ventana.get_left(), ventana.get_right()).shift(DOWN * 0.5)
        )
        self.add(lineas_verticales, lineas_horizontales)

        # Crear un librero en el lado izquierdo
        estante_principal = Rectangle(width=1.2, height=3.5).set_fill(DARK_BROWN, opacity=1)
        estante_principal.to_edge(LEFT).shift(DOWN * 0.5)  # Posicionar el librero a la izquierda
        self.add(estante_principal)

        # Crear los estantes del librero con un bucle for
        for i in range(5):  # Crear 5 estantes
            estante = Line(start=LEFT, end=RIGHT, color=WHITE, stroke_width=4).set_length(1.1)
            estante.move_to(estante_principal.get_top() + DOWN * (0.3 + 0.6 * i))  # Ajustar la posición de cada estante
            self.add(estante)

        # Crear los libros en los estantes
        libros = []
        colores = [RED, COLOR_GELIPE, GREEN, YELLOW]
        for i in range(4):  # Crear libros para 4 estantes
            for j in range(3):  # Tres libros por estante
                libro = Rectangle(width=0.15, height=0.5).set_fill(colores[j % len(colores)], opacity=1)
                libro.move_to(estante_principal.get_top() + DOWN * (0.6 * (i + 1)) + RIGHT * (0.35 * (j - 1)))
                libros.append(libro)
        
        # Añadir todos los libros a la escena
        self.add(*libros)

        # Crear el cuerpo del robot (Gelipe) como una elipse
        cuerpo = Ellipse(width=5, height=2, color=COLOR_GELIPE, fill_opacity=1)
        cuerpo.shift(DOWN * 0.5)  # Ajustar la posición del cuerpo
        self.add(cuerpo)

        # Crear los ojos del robot Gelipe
        ojo1 = Polygon([-0.7, -0.1, 0], [-0.2, -0.1, 0], [-0.45, -0.5, 0], color=WHITE, fill_opacity=1)  # Ojo izquierdo
        ojo2 = Polygon([0.7, -0.1, 0], [0.2, -0.1, 0], [0.45, -0.5, 0], color=WHITE, fill_opacity=1)  # Ojo derecho
        ojo1.shift(LEFT * 0.35 + DOWN * 0.01)  # Posicionar el ojo izquierdo
        ojo2.shift(RIGHT * 0.35 + DOWN * 0.01)  # Posicionar el ojo derecho
        self.add(ojo1)
        self.add(ojo2)

        # Crear los brazos del robot Gelipe
        brazo1 = RoundedRectangle(width=2, height=0.5, color=COLOR_GELIPE, fill_opacity=1)
        brazo2 = RoundedRectangle(width=2, height=0.5, color=COLOR_GELIPE, fill_opacity=1)
        brazo1.rotate(PI / 8)
        brazo2.rotate(-PI / 8)

        brazo1.shift(LEFT * 3 + DOWN * 1)  # Ajustar la posición del brazo izquierdo
        brazo2.shift(RIGHT * 3 + DOWN * 1)  # Ajustar la posición del brazo derecho
        self.add(brazo1)
        self.add(brazo2)

        # Crear las piernas del robot Gelipe
        pierna1 = Square(side_length=0.7, color=COLOR_GELIPE, fill_opacity=1)
        pierna2 = Square(side_length=0.7, color=COLOR_GELIPE, fill_opacity=1)
        pierna1.shift(LEFT * 0.75 + DOWN * 1.7)  # Posicionar la pierna izquierda
        pierna2.shift(RIGHT * 0.75 + DOWN * 1.7)  # Posicionar la pierna derecha
        self.add(pierna1)
        self.add(pierna2)

        # Crear los pies del robot Gelipe
        pie1 = Polygon([0, 0, 0], [0.5, -0.5, 0], [-0.5, -0.5, 0], color=COLOR_GELIPE, fill_opacity=1)  # Pie izquierdo
        pie2 = Polygon([0, 0, 0], [0.5, -0.5, 0], [-0.5, -0.5, 0], color=COLOR_GELIPE, fill_opacity=1)  # Pie derecho
        pie1.shift(LEFT * 0.75 + DOWN * 2.1)  # Posicionar el pie izquierdo
        pie2.shift(RIGHT * 0.75 + DOWN * 2.1)  # Posicionar el pie derecho
        self.add(pie1)
        self.add(pie2)

        # Crear la boca como una flecha curva doble
        flecha_curva_doble = CurvedDoubleArrow(
            start_point=LEFT * 0.8, end_point=RIGHT * 0.8, color=YELLOW, angle=-PI / 2
        )
        flecha_curva_doble.shift(DOWN * 1.2)  # Posicionar la boca (flecha curva) más abajo
        flecha_curva_doble.scale(0.7)  # Ajustar el tamaño de la boca
        self.add(flecha_curva_doble)

        # Agrupar pierna1 y pie1 para moverlos juntos
        pierna_y_pie1 = VGroup(pierna1, pie1)

        # Animación para levantar el brazo derecho y mover la pierna izquierda y el pie juntos
        punto_fijo_brazo2 = brazo2.get_left()  # Mantener este punto fijo para el brazo
        punto_fijo_pierna1 = pierna1.get_top()  # Mantener la parte superior de la pierna como punto de rotación
        punto_fijo_boca1 = flecha_curva_doble.get_top()  # Mantener el punto fijo para la boca

        # Agrupar las animaciones de rotación
        animaciones = AnimationGroup(
            Rotate(brazo2, angle=PI / 3, about_point=punto_fijo_brazo2),  # Levantar el brazo derecho
            Rotate(pierna_y_pie1, angle=-PI / 6, about_point=punto_fijo_pierna1),  # Mover la pierna izquierda
            Rotate(flecha_curva_doble, angle=2 * PI / 2, about_point=punto_fijo_boca1)  # Hacer que la boca sonría
        )

        # Reproducir las animaciones
        self.play(animaciones)
        self.wait(0.5)

        # Animación para regresar a la posición original
        animaciones_invertidas = AnimationGroup(
            Rotate(brazo2, angle=-PI / 3, about_point=punto_fijo_brazo2),  # Bajar el brazo derecho
            Rotate(pierna_y_pie1, angle=PI / 6, about_point=punto_fijo_pierna1),  # Regresar la pierna izquierda
            Rotate(flecha_curva_doble, angle=-2 * PI / 2, about_point=punto_fijo_boca1)  # Regresar la boca a su estado original
        )

        # Reproducir las animaciones de regreso
        self.play(animaciones_invertidas)

        # Esperar antes de finalizar la escena
        self.wait(5)
