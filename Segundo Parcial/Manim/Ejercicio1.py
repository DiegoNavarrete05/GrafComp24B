from manim import *

class OpeningManimExample(Scene):
    def construct(self):
        title = Text("This is some \\LaTeX")
        basel = MathTex(
            r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}"
        )
        
        # Agrupar y organizar el texto
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, shift=UP),
        )
        self.wait()

        # Transformar el título
        transform_title = Text("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(FadeOut(basel), shift=DOWN),
        )
        self.wait()

        # Crear el plano numérico y el título de la cuadrícula
        grid = NumberPlane()
        grid_title = Text("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        # Agregar la cuadrícula y el título
        self.add(grid, grid_title)  
        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=DOWN),
            Write(grid),
        )
        self.wait()

        # Transformar el título de la cuadrícula
        grid_transform_title = Text(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title.get_top() + UP * 0.5)
        
        # Aplicar la transformación no lineal a la cuadrícula
        self.play(
            grid.animate.apply_function(
                lambda p: p + np.array([
                    np.sin(p[1]),
                    np.sin(p[0]),
                    0,
                ])
            ),
            run_time=3,
        )
        self.wait()
        
        # Transformar el título de la cuadrícula
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()