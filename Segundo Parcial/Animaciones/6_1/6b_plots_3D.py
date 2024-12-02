from manim import *
import random
class Aa(Scene):
    def construct(self):
        self.camera.background_color = "#BDD2E4"
        title = Text("""
                    Universidad Autónoma del Estado de México
                    
                            Centro Universitario UAEM Zumpango
                     
                                        Ingeniería en Computación
                     
                                        Graficación Computacional
        """, font_size=28,color=BLACK)
        title.to_edge(UP)
        name_text = Text("Plots 3D", font_size=36, color=BLACK)
        additional_text = Text("""
        Alumno: Diego Argel Navarrete Godines
        
        Profesora: Hazem Álvarez Rodríguez
                
        Periodo: 24B
        """, font_size=24,color=BLACK)
        additional_text.next_to(name_text, ORIGIN + DOWN, buff=1)
    
        self.play(Write(title))
        self.play(FadeIn(name_text))
        self.wait(2)
        self.play(name_text.animate.scale(1.2).set_color(YELLOW))
        self.wait(1)
        self.play(name_text.animate.scale(1/1.2).set_color(BLACK))
        self.wait(1)
        self.play(FadeIn(additional_text))
        self.wait(3)
        
        self.play(FadeOut(name_text), FadeOut(title), FadeOut(additional_text))
        self.wait(1)
        self.camera.background_color = BLACK
class CameraPosition1(ThreeDScene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        circulo = Circle()
        self.play(Create(circulo))
        self.wait()
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class CameraPosition2(ThreeDScene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=0 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class CameraPosition3(ThreeDScene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class CameraPosition4(ThreeDScene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6)
        self.play(Create(circle), Create(axes))
        self.wait()
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class CameraPosition5(ThreeDScene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6, gamma=30 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

#------ Move camera

class MoveCamera1(ThreeDScene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        axes = ThreeDAxes()
        circle = Circle()
        self.play(Create(circle), Create(axes))
        self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait()
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class MoveCamera2(ThreeDScene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=80 * DEGREES, theta=-PI / 2)
        self.wait()
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

#----------- Funciones paramétricas

class ParametricCurve1(ThreeDScene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        curve1 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u / 2
            ]), color=RED, t_range=np.array([-TAU, TAU])
        )
        curve2 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u
            ]), color=RED, t_range=np.array([-TAU, TAU])
        )
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(Create(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func=there_and_back, run_time=3)
        self.wait()
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class ParametricCurve2(ThreeDScene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        curve1 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u / 2
            ]), color=RED, t_range=np.array([-TAU, TAU])
        )
        curve2 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u
            ]), color=RED, t_range=np.array([-TAU, TAU])
        )
        curve1.set_shade_in_3d(True)
        curve2.set_shade_in_3d(True)
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(Create(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func=there_and_back, run_time=3)
        self.wait()
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

#----- Surfaces

class SurfacesAnimation(ThreeDScene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        axes = ThreeDAxes()

        # Crear una serie de superficies
        cylinder = Surface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            u_range=[0, 1],
            v_range=[0, TAU],
            resolution=(6, 32)
        ).fade(0.5)

        paraboloid = Surface(
            lambda u, v: np.array([
                np.cos(v) * u,
                np.sin(v) * u,
                u**2
            ]),
            u_range=[0, 3],
            v_range=[0, TAU],
            resolution=(10, 32)
        ).scale(2)

        para_hyp = Surface(
            lambda u, v: np.array([
                u,
                v,
                u**2 - v**2
            ]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(15, 32)
        ).scale(1)

        cone = Surface(
            lambda u, v: np.array([
                u * np.cos(v),
                u * np.sin(v),
                u
            ]),
            u_range=[0, 2],
            v_range=[0, TAU],
            resolution=(15, 32)
        ).scale(1)

        hip_one_side = Surface(
            lambda u, v: np.array([
                np.cosh(u) * np.cos(v),
                np.cosh(u) * np.sin(v),
                np.sinh(u)
            ]),
            u_range=[-2, 2],
            v_range=[0, TAU],
            resolution=(15, 32)
        )

        ellipsoid = Surface(
            lambda u, v: np.array([
                1 * np.cos(u) * np.cos(v),
                2 * np.cos(u) * np.sin(v),
                0.5 * np.sin(u)
            ]),
            u_range=[-PI / 2, PI / 2],
            v_range=[0, TAU],
            resolution=(15, 32)
        ).scale(2)

        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]),
            u_range=[-PI / 2, PI / 2],
            v_range=[0, TAU],
            resolution=(15, 32)
        ).scale(2)

        # Configuración de la cámara
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        # Añadir las superficies a la escena
        self.add(axes)
        self.play(Write(sphere))
        self.wait()
        self.play(ReplacementTransform(sphere, ellipsoid))
        self.wait()
        self.play(ReplacementTransform(ellipsoid, cone))
        self.wait()
        self.play(ReplacementTransform(cone, hip_one_side))
        self.wait()
        self.play(ReplacementTransform(hip_one_side, para_hyp))
        self.wait()
        self.play(ReplacementTransform(para_hyp, paraboloid))
        self.wait()
        self.play(ReplacementTransform(paraboloid, cylinder))
        self.wait()
        self.play(FadeOut(cylinder))
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

#---- Text on 3D

class Text3D1(ThreeDScene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Text("This is a 3D text").scale(2)
        self.add(axes, text3d)
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class Text3D2(ThreeDScene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Text("This is a 3D text").scale(2).set_shade_in_3d(True)
        text3d.rotate(PI / 2, axis=RIGHT)
        self.add(axes, text3d)
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class Text3D3(ThreeDScene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Text("This is a 3D text")

        self.add_fixed_in_frame_mobjects(text3d)  # <-- Add this
        text3d.to_corner(UL)

        self.add(axes)
        self.begin_ambient_camera_rotation()
        self.play(Write(text3d))

        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]),
            u_range=[-PI / 2, PI / 2],
            v_range=[0, TAU],
            resolution=(15, 32)
        ).scale(2)

        self.play(Write(sphere))
        self.wait()
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
