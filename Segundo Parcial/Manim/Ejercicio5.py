from manim import *

class UdatersExample(Scene):
    def construct(self):
        # Crear un número decimal que irá cambiando
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        # Crear un cuadrado y colocarlo en la parte superior
        square = Square().to_edge(UP)

        # Actualizar la posición del decimal y su valor
        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))

        # Añadir el cuadrado y el número decimal a la escena
        self.add(square, decimal)

        # Animar el movimiento del cuadrado hacia abajo
        self.play(
            square.animate.to_edge(DOWN),
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()
