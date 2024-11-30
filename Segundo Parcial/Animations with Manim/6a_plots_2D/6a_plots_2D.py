from manim import *


class PlotGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[4, 7, 0.5], 
            y_range=[20, 50, 5],
            x_length=10,       
            y_length=6,       
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(4, 7.0+0.5, 0.5)},
            y_axis_config={"numbers_to_include": range(30, 60, 10)},
        ).to_edge(LEFT)

        x_label = MathTex("x").next_to(axes.x_axis, DOWN)
        y_label = MathTex("y").next_to(axes.y_axis, LEFT)
        dot = Dot().move_to(axes.coords_to_point(4, 20))
        self.play(FadeIn(dot))
        self.play(Create(axes), Write(x_label), Write(y_label))
        graph = axes.plot(
            lambda x: x**2,
            x_range=[5,7],
            color=GREEN,
        )
        self.play(Create(graph), run_time=2)
        self.wait()

class Plot1(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 7, 0.5], 
            y_range=[0, 50, 5],
            x_length=10,       
            y_length=6,       
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(2, 7.0+0.5, 0.5)},
            y_axis_config={"numbers_to_include": range(0, 60, 10)},
        ).to_edge(LEFT)

        x_label = MathTex("x").next_to(axes.x_axis, DOWN)
        y_label = MathTex("y").next_to(axes.y_axis, LEFT)
        self.play(Create(axes), Write(x_label), Write(y_label))
        graph = axes.plot(
            lambda x: x**2,
            x_range=[2,4],
            color=GREEN,
        )
        self.play(Create(graph), run_time=2)
        self.wait()


class Plot1v2(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 50, 5],
            axis_config={"color": BLUE},
        )
        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[2, 4])
        
        self.play(Create(axes), Create(graph), run_time=2)
        self.wait()



class Plot2(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 50, 5],
            axis_config={"color": BLUE},
        )
        self.setup_axes(axes)
        graph = axes.plot(lambda x: x**2, color=GREEN)
        
        
        self.play(Create(axes), Create(graph), run_time=2)
        self.wait()

    def setup_axes(self, axes):
        # Parametros de las etiquetas
        init_label_x = 2
        end_label_x = 7
        step_x = 1
        init_label_y = 20
        end_label_y = 50
        step_y = 5

        # Posición de las etiquetas
        axes.x_axis.add_numbers(range(init_label_x, end_label_x + step_x, step_x))
        axes.y_axis.add_numbers(range(init_label_y, end_label_y + step_y, step_y))

        # Animación
        self.play(Create(axes.x_axis), Create(axes.y_axis))


class Plot3(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 50, 10],
            axis_config={"color": BLUE},
        )
        self.setup_axes(axes)
        graph = axes.plot(lambda x: x**2, color=GREEN)

        self.play(Create(axes), Create(graph), run_time=2)
        self.wait()

    def setup_axes(self, axes):
        # Parametros de las etiquetas
        x_labels = [0, 2, 5, 4]
        init_label_y = 0
        end_label_y = 50
        step_y = 5

        # Posición de las etiquetas
        axes.x_axis.add_labels({x: str(x) for x in x_labels})
        axes.y_axis.add_labels({y: str(y) for y in range(init_label_y, end_label_y + step_y, step_y)})

        # Animación
        self.play(Write(axes.x_axis), Write(axes.y_axis))




class Plot4(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 50, 10],
            axis_config={"color": BLUE},
        )
        self.setup_axes(axes)
        graph = axes.plot(lambda x: x**2, color=GREEN)

        self.play(Create(axes), Create(graph), run_time=2)
        self.wait()

    def setup_axes(self, axes):
        # Parametros de las etiquetas
        x_labels = [3.5, 5, 4]
        y_labels = range(0, 55, 5)

        # Posición de las etiquetas
        axes.x_axis.add_labels({x: str(x) for x in x_labels})
        axes.y_axis.add_labels({y: str(y) for y in y_labels})

        # Animación
        self.play(Write(axes.x_axis), Write(axes.y_axis))

from manim import *

class Plot5(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 7, 0.5],
            y_range=[0, 50, 10],
            axis_config={"color": BLUE},
        )
        self.setup_axes(axes)
        graph = axes.plot(lambda x: x**2, color=GREEN)

        self.play(Create(axes), Create(graph), run_time=2)
        self.wait()

    def setup_axes(self, axes):
        # Parametros de las etiquetas
        values_x = [
            (3.5, "3.5"),  # (posición 3.5, etiqueta "3.5")
            (4.5, "\\frac{9}{2}")  # (posición 4.5, etiqueta "9/2")
        ]
        self.x_axis_labels = VGroup()  # Crear un grupo llamado x_axis_labels

        # Posición de las etiquetas
        for x_val, x_tex in values_x:
            tex = MathTex(x_tex)  # Convertir cadena a MathTex
            tex.scale(0.7)
            tex.next_to(axes.c2p(x_val, 0), DOWN)  # Poner MathTex en la posición
            self.x_axis_labels.add(tex)  # Añadir MathTex al gráfico

        # Añadir etiquetas al gráfico
        axes.add(self.x_axis_labels)

        # Animación
        self.play(
            Write(self.x_axis_labels),
            Write(axes.x_axis),
            Write(axes.y_axis)
        )


from manim import *

class Plot6(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 7, 0.5],
            y_range=[0, 50, 10],
            axis_config={"color": BLUE},
        )
        self.setup_axes(axes)
        graph = axes.plot(lambda x: x**2, color=GREEN)

        self.play(Create(axes), Create(graph), run_time=2)
        self.wait()

    def setup_axes(self, axes):
        # Lista de valores de posiciones
        values_decimal_x = [0, 0.5, 1, 1.5, 3.35]
        # Transformar posiciones a etiquetas tex
        list_x = [f"{i}" for i in values_decimal_x]
        # Lista de tuplas de (posición, etiqueta)
        values_x = [(i, j) for i, j in zip(values_decimal_x, list_x)]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = MathTex(x_tex)
            tex.scale(0.7)
            tex.next_to(axes.c2p(x_val, 0), DOWN)
            self.x_axis_labels.add(tex)
        
        # Añadir etiquetas al gráfico
        axes.add(self.x_axis_labels)

        # Animación
        self.play(
            Write(self.x_axis_labels),
            Write(axes.x_axis),
            Write(axes.y_axis)
        )

from manim import *

class Plot7(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 7, 0.5],
            y_range=[0, 50, 10],
            axis_config={"color": BLUE},
        )
        self.setup_axes(axes)
        graph = axes.plot(lambda x: x**2, color=GREEN)

        self.play(Create(axes), Create(graph), run_time=2)
        self.wait()

    def setup_axes(self, axes):
        # Parámetros adicionales
        init_val_x = 0
        step_x = 0.5
        end_val_x = 7
        # Posición de las etiquetas
        values_decimal_x = [i for i in np.arange(init_val_x, end_val_x + step_x, step_x)]
        # Lista de etiquetas
        list_x = [f"{i:.1f}" for i in values_decimal_x]
        # Lista de tuplas de (posición, etiqueta)
        values_x = [(i, j) for i, j in zip(values_decimal_x, list_x)]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = MathTex(x_tex)
            tex.scale(0.7)
            tex.next_to(axes.c2p(x_val, 0), DOWN)
            self.x_axis_labels.add(tex)
        
        # Añadir etiquetas al gráfico
        axes.add(self.x_axis_labels)

        # Animación
        self.play(
            Write(self.x_axis_labels),
            Write(axes.x_axis),
            Write(axes.y_axis)
        )


from manim import *
import numpy as np

class PlotSinCos(Scene):
    def construct(self):
        # Configuración de los ejes
        axes = Axes(
            x_range=[-3 * PI / 2, 3 * PI / 2, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE},
        )

        # Añadir etiquetas y personalización de ejes
        self.setup_axes(axes)

        # Graficar seno y coseno
        plot_sin = axes.plot(lambda x: np.sin(x), color=GREEN, x_range=[-3 * PI / 2, 3 * PI / 2])
        plot_cos = axes.plot(lambda x: np.cos(x), color=GRAY, x_range=[-PI, 0])
        plot_sin.set_stroke(width=3)
        plot_cos.set_stroke(width=2)

        # Animaciones
        self.play(Create(axes), run_time=2)
        for plot in (plot_sin, plot_cos):
            self.play(Create(plot), run_time=2)

        self.wait()

    def setup_axes(self, axes):
        # Personalización de ejes
        axes.x_axis.set_stroke(width=2, color=RED)
        axes.y_axis.set_stroke(width=2, color=YELLOW)

        # Añadir etiquetas a los ejes
        func_label = MathTex("\\sin\\theta").set_color(BLUE).next_to(axes.y_axis, UP)
        var_label = MathTex("\\theta").set_color(PURPLE).next_to(axes.x_axis, RIGHT + UP)

        # Etiquetas del eje Y
        axes.y_axis.add_labels({-1: "-1", 1: "1"})

        # Etiquetas del eje X
        x_labels = {
            -3 * PI / 2: "-\\frac{3\\pi}{2}",
            -PI: "-\\pi",
            -PI / 2: "-\\frac{\\pi}{2}",
            0: "0",
            PI / 2: "\\frac{\\pi}{2}",
            PI: "\\pi",
            3 * PI / 2: "\\frac{3\\pi}{2}",
        }

        labels = VGroup()
        for x_val, x_tex in x_labels.items():
            label = MathTex(x_tex).scale(0.7)
            label.next_to(axes.c2p(x_val, 0), DOWN if x_val != -PI and x_val != PI else 2 * DOWN)
            labels.add(label)

        # Animación de la configuración
        self.play(
            Write(axes.y_axis),
            Write(axes.x_axis),
            Write(labels),
            Write(func_label),
            Write(var_label),
            run_time=2,
        )
