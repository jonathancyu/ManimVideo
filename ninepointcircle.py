from manim import *
import math

class PartB(Scene):
    def construct(self):
        # section a
        self.group = VGroup()

        # Triangle
        A = np.array([-1, 1, 0])
        B = np.array([-2, -2, 0])
        C = np.array([4, -2, 0])

        triangle = Polygon(A, B, C)
        self.play(Create(triangle))
        G = self.make_centroid(A, B, C)
        self.move_point(G)
    
    def make_centroid(self, A, B, C):
        m_AB = (A + B)/2
        m_BC = (B + C)/2
        m_AC = (A + C)/2

        perp_bisector_group = VGroup(
            Line(m_AB, C, stroke_width=2),
            Line(m_BC, A, stroke_width=2),
            Line(m_AC, B, stroke_width=2)
        )
        self.play(Create(perp_bisector_group))

        centroid = (A + B + C)/3
        centroid_point = Dot(color=RED).move_to(centroid)
        centroid_label = MathTex("G").move_to(centroid + [-0.3, 0, 0])
        self.play(Create(centroid_point))
        self.play(FadeOut(perp_bisector_group))
        self.play(Write(centroid_label))
        return centroid_point

    def move_point(self, G):
        center = G.get_center()
        startpos = center + [-1, 0.5, 0]
        M = Dot(color=GREEN).move_to(startpos)
        line = Line(G.get_center(), M.get_center())
        x = ValueTracker(startpos[0])
        y = ValueTracker(startpos[1])
        M.add_updater(lambda z: z.move_to([x.get_value(), y.get_value(), 0]))
        M.add_updater(lambda z: z.move_to([y.get_value(), y.get_value(), 0]))
        line.add_updater(lambda z: z.become(Line(G.get_center(), M.get_center())))
        self.play(Create(M))
        self.play(Create(line))
        for pos in [(-2, 0), (2, 0), (0, 2)]:#[(-0.6, -0.6), (-1, 0.5), (1, -0.4)]:
            self.play(x.animate.set_value(center[0] + pos[0]), 
                      y.animate.set_value(center[1] + pos[1]))
            self.wait(0.5)