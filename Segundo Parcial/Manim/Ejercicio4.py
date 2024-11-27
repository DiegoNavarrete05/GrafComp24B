from manim import *

class WriteStuff(Scene):
    def construct(self):
        # Crear texto simple y dividir en partes
        example_text = Text("This is some text")
        example_text[10:14].set_color(YELLOW)  # Cambiar el color de la palabra "text"

        # Crear texto matemático
        example_tex = MathTex(
            r"\sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6}",
        )
        
        # Agrupar los textos
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(config.frame_width - 2 * LARGE_BUFF)

        # Animar la escritura de los textos
        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()

# Para ejecutar esta escena, usa el siguiente comando:
# manim -pql write_stuff.py WriteStuff
